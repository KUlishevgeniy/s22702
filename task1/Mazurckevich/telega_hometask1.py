import telebot
import psycopg2
from telebot import types

bot=telebot.TeleBot('6129933621:AAF3mMe2Ftdx-WNgMNRsuFmqG_Bt3wtl6GE')

connection = psycopg2.connect(host= 'localhost', dbname='data', user='postgres', password='Q1w2e3r4')
cursor=connection.cursor()

#Функция обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Вывести весь список")
    item2=types.KeyboardButton("Вывести конкретный номер списка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Привет! \n\n Этот бот позволяет увидеть первые 100 предложений на Авито по запросу "Дизайнер презентаций" \n\n Бот способен вывести весь список выпадающих предложений или же конкретный номер списка. \n\n Нажми на кнопку и проверь!', reply_markup=markup)
#получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    #Если юзер нажал 1
    if message.text.strip() == 'Вывести весь список':
        select_qwery = f"""SELECT place, naming, price, image FROM public.hometask_table;"""
        cursor.execute(select_qwery)
        for row in cursor.fetchall():
            place = row[0]
            naming = row[1]
            price = row[2]
            image = row[3]
            bot.send_message(message.chat.id, "%d %s %s %s" %(place, naming, price, image))
            #break
    #Если юзер нажал 2
    elif message.text.strip() == 'Вывести конкретный номер списка':
        markup = telebot.types.ReplyKeyboardMarkup(True)
        msg = bot.send_message(message.from_user.id, 'Какой номер нужно вывести?', reply_markup = markup)
        bot.register_next_step_handler(msg, after_text_2);

    #если юзер тупой
    else: bot.send_message(message.chat.id,'Нет, нужно выбрать из предложенных вариантов. Попробуй ещё.')
 #вывод номера из таблицы
def after_text_2(message):
    number = message.text
    try:
        tmp = int(number)
        select_qwery = f"""SELECT place, naming, price, image FROM public.hometask_table WHERE place = %d;""" %(tmp)
        cursor.execute(select_qwery)
        for row in cursor.fetchall():
            place = row[0]
            naming = row[1]
            price = row[2]
            image = row[3]
            bot.send_message(message.chat.id, "%d %s %s %s" %(place, naming, price, image))
    except:
        markup = telebot.types.ReplyKeyboardMarkup(True)
        msg = bot.send_message(message.from_user.id, 'Вы ввели не число. Какой номер нужно вывести?', reply_markup=markup)
        bot.register_next_step_handler(msg, after_text_2);

#запуск бота
bot.polling(none_stop=True, interval=0)