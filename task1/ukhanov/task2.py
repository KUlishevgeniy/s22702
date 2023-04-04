import telebot
bot = telebot.TeleBot('5908521472:AAHfMOWoCfAGD65kEPSbdM5GVbRhi3wxy3Q')
@bot.message_handler(ccommands=["start"])
def start(m, res=False):
    bot.send_massage(m.chat.id, 'Я готов! Напиши мне')
bot.polling(none_stop=True, interval=0)
@bot.message_handlers(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали:' + message.text)
    bot.polling(none_stop=True, interval=0)

