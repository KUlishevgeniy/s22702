import telebot
import psycopg2
from telebot import types


bot = telebot.TeleBot('5973186472:AAF1o2G2xmLuU3cq7wGOdOwoue0SzfHLNl4')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Полный список")
    item2 = types.KeyboardButton("Выбрать номер")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, "Нажми: \n'Полный список' для того, чтобы увидеть Топ-100 книг "
                                "\n'Выбрать номер' для получения книги на соответствующем месте", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    slovo=message.text

    if slovo == 'Полный список':
        connection = psycopg2.connect(host='localhost', dbname='hwdata',
                                      user='postgres', password='Q1w2e3r4')
        cursor = connection.cursor()
        request = "select * from books"
        cursor.execute(request)
        basa = cursor.fetchall()
        print(basa)
        asd=[]

        for i in range(100):
            k=0


            asd.append(basa[i])



            bot.send_message(message.chat.id, f'{asd[i]}\n')

    elif message.text.strip() == "Выбрать номер":
        send = bot.send_message(message.chat.id, "Введите номер:")
        bot.register_next_step_handler(send, pick_a_number)

@bot.message_handler(content_types=["text"])
def pick_a_number(number):
    id = int(number.text)
    try:
        connection = psycopg2.connect(host='localhost', dbname='hwdata',
                                      user='postgres', password='Q1w2e3r4')
        cursor = connection.cursor()
        request = f"select * from books where id = {id}"
        cursor.execute(request)
        basa = cursor.fetchall()
        bot.send_message(number.chat.id, f"{basa[0][0]}\nНазвание - {basa[0][1]}\nАвтор - {basa[0][2]}")
    except IndexError:
        bot.send_message(number.chat.id, "Число находится вне границ массива, попробуйте от 1 до 100.")


bot.polling(none_stop=True, interval=0)
