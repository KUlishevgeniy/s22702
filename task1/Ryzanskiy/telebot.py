import telebot
import psycopg2
bot=telebot.TeleBot('6047293314:AAGW8F5wDseQ1xiysBreIeb4gzl5pWHjyvM')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'input number')

@bot.message_handler (content_types=["text"])
def handle_text(message):
    video_id1=int(message.text)

    connection = psycopg2.connect(host='localhost', dbname='youtube',
                                  user='postgres', password='3107asdzxc')
    cursor = connection.cursor()
    request = f"select * from youtube where rang = {video_id1}"
    cursor.execute(request)
    b = cursor.fetchall()
    print(b[0][0])
    bot.send_message(message.chat.id, f"rang = {b[0][0]}\nname = {b[0][1]}\nchannel = {b[0][2]}\nviews = {b[0][3]}")
bot.polling(none_stop=True, interval=0)
