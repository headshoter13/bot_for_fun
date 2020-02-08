import telebot

TOKEN = "919944593:AAEUsptIALtikuljlGV47xzXXMCsuhXa8Lk"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Скоро мы построим построим дом-треугольник!")


@bot.message_handler(commands=['checklist'])
def send_welcome(message):
	bot.reply_to(message, "Купи чек-лист, помоги Базалушке подняться!")


@bot.message_handler(content_types=['text'])
def text_handler(message):
	text = message.text.lower()
	chat_id = message.chat.id
	if text == "привет":
		bot.send_message(chat_id, '"Здравствуйте" нужно говорить.')
	elif text == "как дела?":
		bot.send_message(chat_id, 'Пока не родила!')
	elif text == "доброе утро":
		bot.send_message(chat_id, 'Хуютро')
	else:
		bot.send_message(chat_id, 'Простите, я вас не поняла, но на всякий случай, Идите Нахуй!')


bot.polling(none_stop=True)
