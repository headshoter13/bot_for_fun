import telebot

bot = telebot.TeleBot("919944593:AAEUsptIALtikuljlGV47xzXXMCsuhXa8Lk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")