from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import wget
import telebot
from telebot import types
import time
import psycopg2


def parser():
    s = Service('/Users/barykingeorgij/Documents/chromedriver/chromedriver')
    browser = webdriver.Chrome(service=s)
    place = 0
    data = []
    for page in range(1, 6):
        browser.get(f'https://www.kinopoisk.ru/lists/movies/series-top250/?page={page}')
        html_text = browser.page_source
        soup = BeautifulSoup(html_text, 'lxml')
        series = soup.find_all("div", class_="styles_root__ti07r")
        for element in series:
            place += 1
            # Скачиваем фото
            url = element.find("a", class_="base-movie-main-info_link__YwtP1").get("href")
            browser.get("https://www.kinopoisk.ru" + url)
            html_text = browser.page_source
            soup = BeautifulSoup(html_text, 'lxml')
            url = soup.find("img", class_="film-poster")
            wget.download("https:" + url.get("src"), f"img/series{place}.jpeg")

            # Находим нужные нам данные
            rutitle = element.find("span", class_="styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").get_text()
            # У русских сериалов нет английский названий
            try:
                entitle = element.find("span", class_="desktop-list-main-info_secondaryTitle__ighTt").get_text()
            except AttributeError:
                entitle = "---"
            text = element.find("span", class_="desktop-list-main-info_secondaryText__M_aus").get_text()
            mark = element.find("span",
                                class_="styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU").get_text()
            data.append(f"""{place}| {rutitle}| {entitle.replace("'", "")}| {text.replace(",", "")}| {mark}""")
    browser.close()
    return data


def database_insert(data):
    connection = psycopg2.connect(host="localhost", dbname="PostgreSQL 15", user="postgres", password="123")
    cursor = connection.cursor()
    for i in range(len(data)):
        place, rutitle, entitle, text, mark = data[i].split('|')
        insert_query = f"""INSERT INTO "SERIES"
                           VALUES ('{place}', '{rutitle}', '{entitle}', '{text}', '{mark}');"""
        cursor.execute(insert_query)
    connection.commit()


def database_get(place):
    connection = psycopg2.connect(host="localhost", dbname="PostgreSQL 15", user="postgres", password="123")
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM "SERIES"
                               WHERE place = '{place}'""")
    answer = cursor.fetchall()
    return f'Место - {answer[0][0].strip()}\n\nРусское название - {answer[0][1].strip()}\n\n' \
           f'Английское название - {answer[0][2].strip()}\n\n{answer[0][3].strip()}\n\n' \
           f'Оценка - {answer[0][4].strip()}'


def load():
    bot = telebot.TeleBot("6145872070:AAHwvoflTxtFPLZ4fkpTQpY_W6x_5woGb5Q")

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("Список Сериалов")
        markup.add(button)
        bot.send_message(m.chat.id, "Добро пожаловать!\nДанный бот выводит список сериалов из кинопоиска.",
                         reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Список Сериалов':
            send = bot.send_message(message.chat.id, "Сколько сериалов вывести? (1 - 250)")
            bot.register_next_step_handler(send, series_print)
        else:
            bot.send_message(message.chat.id, "Нажмите на кнопки")

    @bot.message_handler(content_types=["text"])
    def series_print(message):
        print(message.text)
        try:
            if int(message.text) in range(1, 251):
                for i in range(1, int(message.text) + 1):
                    answer = database_get(i)
                    time.sleep(1)
                    img = open(f'img/series{i}.jpeg', 'rb')
                    bot.send_photo(message.chat.id, img, caption=f'{answer}')
            else:
                bot.send_message(message.chat.id, "Ошибка 1")
        except:
            bot.send_message(message.chat.id, "Ошибка 2")

    bot.polling(none_stop=True, interval=0)


def main():
    data = parser()
    database_insert(data)
    load()


main()
