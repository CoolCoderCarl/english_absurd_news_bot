import telebot
import random
import problems
import discovered
import someone
import solutions
import reporters

bot = telebot.TeleBot(token="NOTOKENHERE")

@bot.message_handler(commands=['start'])
def send_welcome(message):

	welcome = ("""
		Hello ! Send /news and have fun.
		""")

	bot.send_message(message.chat.id, welcome)


@bot.message_handler(commands=['news'])
def send_news(message):

	randomNews = ("INNOVATION !!!" + "\n" +
			"=====================================================" + "\n" +
			"There were discovered " + random.choice(problems.problems) +
			" " + random.choice(discovered.when) +
			" and " + random.choice(someone.clever) +
			" decide to " + random.choice(solutions.solutions) + "\n" +
			"=====================================================" + "\n" +
			"The reporter is: " + random.choice(reporters.reporter))

	bot.send_message(message.chat.id, randomNews)

	bot.send_poll(message.chat.id, "Do you like this news ?", ["Yes", "No", "Kurwa !", "I do not know any english word"],
				  is_anonymous=False)

@bot.message_handler(commands=['help'])
def help(message):
	helpMessage = """
		Hello there, I am Random News Generator Bot. Sometimes i help the politicians, but usually i entertain the common people. For getting news send me command like /news or /news@english_absurd_news_bot and have fun.
		"""

	bot.send_message(message.chat.id, helpMessage)

bot.polling()