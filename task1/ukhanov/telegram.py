import telebot
import random
from telebot input types
bot = telebot.TeleBot('5908521472:AAHfMOWoCfAGD65kEPSbdM5GVbRhi3wxy3Q')
f = open('')
facts = f.read().split('\n')
f.close()
f = open('')
thinks = f.read().split('\n')
f.close()
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я готов. Напиши мне что то');
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    bot.send_message(m.chat.id, 'Нажми: \n')