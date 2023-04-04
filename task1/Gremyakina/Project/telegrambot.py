import telebot
import Database
from telebot import types
import time


def create_bot():
    bot = telebot.TeleBot("6275487502:AAEPogpoQZtetHZu6hNewYIhlA_vYIBQOTg")

    @bot.message_handler(commands = ["start"])
    def start(m, res = False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        About_button = types.KeyboardButton("Что ты делаешь?")
        Films_button = types.KeyboardButton("Покажи список фильмов")
        markup.add(About_button)
        markup.add(Films_button)
        bot.send_message(m.chat.id, "Привет!!!", reply_markup = markup)

    @bot.message_handler(content_types = ["text"])
    def handle_text(message):
        if message.text.strip() == "Что ты делаешь?":
            bot.send_message(message.chat.id, "Показываю список фильмов!")
        elif message.text.strip() == "Покажи список фильмов":
            for i in range(1, 251):
                ans = Database.get(i)
                print(ans)
                time.sleep(1)
                bot.send_message(message.chat.id, ans)
                img = open(f'pics/{i}.jpeg', 'rb')
                bot.send_photo(message.chat.id, img)
        else:
            bot.send_message(message.chat.id, "Нажмите на кнопку.")

    bot.polling(none_stop= True, interval= 0)


