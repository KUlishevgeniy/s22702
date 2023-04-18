import telebot
import random
import psycopg2
from telebot import types

bot=telebot.TeleBot('6129933621:AAF3mMe2Ftdx-WNgMNRsuFmqG_Bt3wtl6GE')

connection = psycopg2.connect(host= 'localhost', dbname='data', user='postgres', password='Q1w2e3r4')
cursor=connection.cursor()

#Функция обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Вывести весь список")
    item2=types.KeyboardButton("Вывести конкретный номер списка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми \nВывести весь список чтобы увидеть все результаты по запросу "дизайнер презентаций" на Авито\nВывести конкретный номер списка чтобы увидеть конкретный номер этого списка', reply_markup=markup)
#получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = 'Пустой запрос'
    #Если юзер нажал 1
    if message.text.strip() == 'Вывести весь список':
        select_qwery = f"""SELECT place, naming, price, image FROM public.hometask_table;"""
        cursor.execute(select_qwery)
        textout_list = cursor.fetchall()
        for i in range(0, len(textout_list)):
            print(textout_list[i])

            if textout_list[i] > textout_list[i + 1]: pass

    #Если юзер нажал 2
    elif message.text.strip() == 'Вывести конкретный номер списка':
        select_qwery = f"""SELECT place, naming, price, image FROM public.hometask_table;"""
        cursor.execute(select_qwery)
    #Отсылаем сообщение в чат
    bot.send_message(message.chat.id, )

#запуск бота
bot.polling(none_stop=True, interval=0)

#запарсить данные в таблицу, в телеграмм боте выдывать записанные данные по записанному айди