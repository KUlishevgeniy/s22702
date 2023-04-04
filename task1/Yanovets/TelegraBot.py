import telebot
import random

from telebot import types

bot = telebot.TeleBot('6214235613:AAHX1KT6io6Mmo_j4zXZNgq_hWpbXqwri7U')
f = open('data/facts', 'r',encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open('data/thinks', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button1 = types.KeyboardButton("Факт")
    button2 = types.KeyboardButton("Премудрость")
    markup.add(button1)
    markup.add(button2)
    bot.send_message(m.chat.id, "Курлык-курлык")
    bot.send_message(m.chat.id, 'Наконец-то веселые приколы!', reply_markup= markup);
@bot.message_handler(content_types=["text"])
def hantle_text(message):
    bot.send_message(message.chat.id, 'Вы написали... ' + message.text)
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Премудрость':
        answer = random.choice(thinks)
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)
#jjj