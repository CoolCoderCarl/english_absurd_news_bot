import os
import random
import telebot
import items.problems
import items.discovered
import items.someone
import items.solutions
import items.reporters
import items.titles

api_token = os.environ['API_TOKEN']
bot = telebot.TeleBot(token=api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):

	welcome = ("""
		Hello ! Send /news and have fun.
		""")

	bot.send_message(message.chat.id, welcome)


@bot.message_handler(commands=['news'])
def send_news(message):

	randomNews = (random.choice(items.titles.titles) + "\n" +
			"=====================================================" + "\n" +
			"There were discovered " + random.choice(items.problems.problems) +
			" " + random.choice(items.discovered.when) +
			" and " + random.choice(items.someone.clever) +
			" decide that " + random.choice(items.solutions.solutions) + "\n" +
			"=====================================================" + "\n" +
			"The reporter is: " + random.choice(items.reporters.reporter))

	bot.send_message(message.chat.id, randomNews)

	bot.send_poll(message.chat.id, "Do you like this news ?", ["Yes", "No", "Kurwa !", "Evil enemies !", "Praise the Queen"],
				  is_anonymous=False)

@bot.message_handler(commands=['help'])
def help(message):
	helpMessage = """
		Hello there, I am Random News Generator Bot. Sometimes i help the politicians, but usually i entertain the common people. For getting news send me command like /news or /news@english_absurd_news_bot and have fun.
		"""

	bot.send_message(message.chat.id, helpMessage)

bot.polling()
