#import asyncio
#import time
import telebot
from telebot import types
bot = telebot.TeleBot('5390890783:AAHgTuMn3jqD-yb8H5xc3uU0k7-C_krfQqU')

@bot.message_handler(commands = ["start"])
def start(message):
	mess = message.from_user.first_name
	bot.send_message(message.chat.id, '<b>Hello {0}</b>'.format(mess), parse_mode = "html")

@bot.message_handler(commands = ["info"])
def info(message):
	bot.send_message(message.chat.id, message)


@bot.message_handler(commands = ["weather"])
def weather(message):
	markup = types.ReplyKeyboardMarkup()
	website = types.KeyboardButton("Web")
	startus = types.KeyboardButton("start")
	markup.add(website, startus)
	bot.send_message(message.chat.id, "nothinfg", reply_markup = markup)


bot.polling(none_stop = True)