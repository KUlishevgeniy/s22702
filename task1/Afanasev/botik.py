import psycopg2
import  telebot

bot = telebot.TeleBot('6190221581:AAGKpgeL1cY8FaE28_O4mA4AwAsG6iqMlcc')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Введите число от 0-14')

@bot.message_handler (content_types=["text"])
def handle_text(message):
    id=int(message.text)

    connection = psycopg2.connect(host='localhost', dbname='db',
                                  user='postgres', password='q1w2e3r4')
    cursor = connection.cursor()
    request = f"select * from travel where id = {id}"
    cursor.execute(request)
    b = cursor.fetchall()
    bot.send_message(message.chat.id, f"{b[0][1]}\n {b[0][2]}\n {b[0][3]}\n {b[0][4]}\n")
bot.polling(none_stop=True, interval=0)




