import psycopg2
import  telebot
import random
from telebot import types

connection = psycopg2.connect(host='localhost', dbname='db', user='postgres', password='qwerty')
cursor=connection.cursor()

sqlite_select_query = """SELECT * from cars"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()

bot = telebot.TeleBot('6193959892:AAGyaLPtXHUq7vAI2ra4VMOqc86YiJdgQX0')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item=types.KeyboardButton("Машинка")
    markup.add(item)
    bot.send_message(m.chat.id, 'Нажми: \nМашинка '
                     'чтобы выбрать произвольную машинку',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Машинка':
            answer = random.choice(records)
    for i in answer:
        i = str(i)
        bot.send_message(message.chat.id, i.strip())
    #bot.send_photo(message.chat.id, f"imagine\{answer[0]}.jpg")
bot.polling(none_stop=True, interval=0)



