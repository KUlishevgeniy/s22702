import telebot
import psycopg2
bot=telebot.TeleBot('6104092270:AAEzX5Yx93HFA6BPGLj9qRUtczrUrJgDCno')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'молодчина')

@bot.message_handler (content_types=["text"])
def handle_text(message):
    car_id1=int(message.text)

    connection = psycopg2.connect(host='localhost', dbname='auto',
                                  user='postgres', password='3107asdzxc')
    cursor = connection.cursor()
    request = f"select * from auto where id = {car_id1}"
    cursor.execute(request)
    b = cursor.fetchall()
    print(b[0][0])
    bot.send_message(message.chat.id, f"ID = {b[0][0]}\nБренд = {b[0][1]}\nЦена = {b[0][2]}")
bot.polling(none_stop=True, interval=0)





