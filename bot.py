import telebot
import newsGen

randomNews = newsGen.newsGen()

bot = telebot.TeleBot(token="NOTOKENHERE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, randomNews)

bot.polling()