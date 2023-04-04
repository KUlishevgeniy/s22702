import telebot
import DBOperator
from telebot import types
import time


def load():
    bot = telebot.TeleBot("5740447185:AAFP-u008ZlkcRkJ8mkR2aasXM3GX4UBA9I")

    @bot.message_handler(commands = ["start"])
    def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        About_btn = types.KeyboardButton("Для чего ты нужен?")
        Films_btn = types.KeyboardButton("Список фильмов")
        Games_btn = types.KeyboardButton("Список игр")
        markup.add(About_btn)
        markup.add(Films_btn)
        markup.add(Games_btn)
        bot.send_message(m.chat.id, "Добро пожаловать!\nДанный бот выводит список фильмов из кинопоиска, либо список игр!", reply_markup= markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Для чего ты нужен?':
            bot.send_message(message.chat.id, "Чтобы выдавать фильмы и игры!")
        elif message.text.strip() == 'Список фильмов':
            send = bot.send_message(message.chat.id, "Сколько фильмов вывести? (1 - 250)")
            bot.register_next_step_handler(send, film_print)
        elif message.text.strip() == 'Список игр':
            send = bot.send_message(message.chat.id, "Сколько игр вывести? (1 - 512):")
            bot.register_next_step_handler(send, game_print)
        else:
            bot.send_message(message.chat.id, "Нажмите на кнопки")

    @bot.message_handler(content_types=["text"])
    def film_print(message):
        print(message.text)
        try:
            if int(message.text) in range(1, 251):
                for i in range(1, int(message.text) + 1):
                    answer = DBOperator.get_films(i)
                    print(answer)
                    time.sleep(1)
                    img = open(f'Pictures/FILMS/FILM{i}.jpeg', 'rb')
                    bot.send_photo(message.chat.id, img, caption=f'{answer}')
            else:
                bot.send_message(message.chat.id, "Число не находится в диапазоне от 1 до 250")
        except:
            bot.send_message(message.chat.id, "Введи число, а не набор символов")

    @bot.message_handler(content_types=["text"])
    def game_print(message):
        print(message.text)
        try:
            if int(message.text) in range(1, 513):
                for i in range(1, int(message.text) + 1):
                    answer = DBOperator.get_games(i)
                    print(answer)
                    time.sleep(1)
                    img = open(f'Pictures/GAMES/GAME{i}.jpeg', 'rb')
                    bot.send_photo(message.chat.id, img)
                    bot.send_message(message.chat.id, answer)
            else:
                bot.send_message(message.chat.id, "Число не находится в диапазоне от 1 до 512")
        except:
            bot.send_message(message.chat.id, "Введи число, а не набор символов")

    bot.polling(none_stop = True, interval = 0)


if __name__ == "__main__":
    load()