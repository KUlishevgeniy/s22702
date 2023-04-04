import telebot
from telebot import types
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import wget
import psycopg2


def load():
    bot = telebot.TeleBot("6259563116:AAH5-5pD3d8NT_XaQmWunPh3PLoFrjKAvvA")
    connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="628230")
    cursor = connection.cursor()

    @bot.message_handler(commands = ["start"])
    def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        films = types.KeyboardButton("Список фильмов")
        markup.add(films)
        bot.send_message(m.chat.id, "Добро пожаловать!\n", reply_markup= markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Список фильмов':
            for place in range(1, 251):
                cursor.execute(f"""SELECT * FROM "testdb"
                                       WHERE id = {place}""")
                answer = cursor.fetchall()[0]
                answer = f"МЕСТО - {answer[0]}\nНАЗВАНИЕ - {answer[1]}\nАНГЛИЙСКОЕ НАЗВАНИЕ, ДАТА И ХРОНОМЕТРАЖ - {answer[2]}\nОЦЕНКА - {answer[3]}"
                print(answer)
                time.sleep(1)
                img = open(f'pics/{place}.jpeg', 'rb')
                bot.send_photo(message.chat.id, img, caption=f'{answer}')

    bot.polling(none_stop = True, interval = 0)


def main():
    #Соединяемся с базой данных
    connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="628230")
    cursor = connection.cursor()

    answer = ''
    while (answer != 'y') and (answer != 'n'):
        answer = input('Спарсить сайт? (y / n)\n')
    if answer == 'y':
        s = Service('D:\webdriver\chromedriver.exe')
        browser = webdriver.Chrome(service=s)
        place = 0
        for page in range(1, 6):
            browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={page}')
            time.sleep(10)
            html_text = browser.page_source
            soup = BeautifulSoup(html_text, 'lxml')
            films = soup.find_all("div", class_="styles_root__ti07r")
            for film in films:
                place += 1
                # Скачиваем фото
                url = film.find("a", class_="base-movie-main-info_link__YwtP1").get("href")
                browser.get("https://www.kinopoisk.ru" + url)
                html_text = browser.page_source
                soup = BeautifulSoup(html_text, 'lxml')
                url = soup.find("img", class_="film-poster")
                wget.download("https:" + url.get("src"), f"pics/{place}.jpeg")

                #Собираем данные
                name = film.find("span",
                                          class_="styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").get_text()
                data = film.find("div", class_="desktop-list-main-info_secondaryTitleSlot__mc0mI").get_text()
                mark = film.find("span",
                                 class_="styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU").get_text()

                #Записываем фильм в базу данных
                insert_query = f"""INSERT INTO "testdb"
                                           VALUES ({place}, '{name}', '{data.replace("'", "")}', '{mark}');"""
                cursor.execute(insert_query)
                connection.commit()

        browser.close()

    load()


if __name__ == "__main__":
    main()
