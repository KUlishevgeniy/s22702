import telebot
import random

from telebot import types
#загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
#загружаем список mыслей
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

bot=telebot.TeleBot('6129933621:AAF3mMe2Ftdx-WNgMNRsuFmqG_Bt3wtl6GE')
#Функция обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Факт")
    item2=types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми \nФакт для получения факта\nПоговорка для поговорки', reply_markup=markup)
#получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = '1'
    #Если юзер нажал 1 выдаем случайный факт
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    #Если юзер нажал 2 выдаем мысль
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    #Отсылаем сообщение в чат
    bot.send_message(message.chat.id, answer)

#запуск бота
bot.polling(none_stop=True, interval=0)

#запарсить данные в таблицу, в телеграмм боте выдывать записанные данные по записанному айди