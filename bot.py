import config
import telebot
import os
import time
from telebot import types
import game_play

bot = telebot.TeleBot(config.token)

#starting
@bot.message_handler(commands=["start"])
def start_conversation(message):
	bot.send_message(message.chat.id, "Hello, " + message.from_user.first_name + "!")

#choosing something
@bot.message_handler(commands=["choose"])
def choose_something(message):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.row('1', '2', '3')
	bot.send_message(message.chat.id, "What number do you want to choose?", reply_markup=markup)

#returning result
@bot.message_handler(func=lambda message: True, content_types=['text'])
def return_answer(message):
	text_result = game_play.check_number_and_return_result(int(message.text))
	bot.send_message(message.chat.id, text_result)

if __name__ == '__main__':
    bot.polling(none_stop=True)