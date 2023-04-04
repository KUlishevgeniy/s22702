import telebot
import random
from telebot import types
bot = telebot.TeleBot("5740447185:AAFP-u008ZlkcRkJ8mkR2aasXM3GX4UBA9I")

f = open("data/facts.txt", "r", encoding="UTF-8")
facts = f.read().split('\n')
f.close()

f = open("data/prikoli.txt", "r", encoding="UTF-8")
rofl = f.read().split('\n')
f.close()


@bot.message_handler(commands = ["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("Факт")
    button2 = types.KeyboardButton("Прикол")
    markup.add(button1)
    markup.add(button2)
    bot.send_message(m.chat.id, "SALAM", reply_markup= markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = ""
    bot.send_message(message.chat.id, "Вы написали: " + message.text)
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    if message.text.strip() == 'Прикол':
        answer = random.choice(rofl)
    if answer != "":
        bot.send_message(message.chat.id, answer)




bot.polling(none_stop = True, interval = 0)