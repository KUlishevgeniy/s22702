import psycopg2
import  telebot
import random
from telebot import types

connection = psycopg2.connect(host='localhost', dbname='db', user='postgres', password='q1w2e3r4')
cursor=connection.cursor()

sqlite_select_query = """SELECT * from travel"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()

bot = telebot.TeleBot('6190221581:AAGKpgeL1cY8FaE28_O4mA4AwAsG6iqMlcc')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item=types.KeyboardButton("Тур")
    markup.add(item)
    bot.send_message(m.chat.id, 'Нажми: \nТур'
                     'чтобы выбрать произвольный тур из списка',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Тур':
            answer = random.choice(records)
    for i in answer:
        i = str(i)
        bot.send_message(message.chat.id, i.strip())
    #bot.send_photo(message.chat.id, f"imagine\{answer[0]}.jpg")
bot.polling(none_stop=True, interval=0)




