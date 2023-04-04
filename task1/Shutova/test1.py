import telebot
bot = telebot.TeleBot('6245079764:AAFaEzF4YW7UiecEMfsTX6Yj7WhF8b2IR5w')
@bot.message_handler(commands=["start"])
def start (m, res=False):
    bot.send_message(m.chat.id, 'Привет) Ты красотка!)')
bot.polling(none_stop=True, interval=0)