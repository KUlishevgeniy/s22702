import telebot
import psycopg2
bot=telebot.TeleBot('6057239448:AAHlqg8bzFRqDBVWty-RuLZFnyDjU3XVB40')
@bot.message_handler (content_types=["text"])
def handle_text(message):
    song_id1=int(message.text)
    connection = psycopg2.connect(host='localhost', dbname='music',
                                  user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    request = f"select * from topmusic where id = {song_id1}"
    cursor.execute(request)
    b = cursor.fetchall()
    bot.send_message(message.chat.id, f" {b[0][1]} - {b[0][2]}")
bot.polling(none_stop=True, interval=0)