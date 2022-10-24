import os

import telebot
from loguru import logger

from constants import keyboards
import emoji


class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['NASHENAS'])
		self.echo_all = self.bot.message_handler(
			func=lambda m: True
		)(self.echo_all)

	def run(self):
		logger.info('Bot is running')
		self.bot.infinity_polling()

	# def echo_all(self, message):
	# 	write_json(message.json, '../message.json')
	# 	self.bot.reply_to(message, message.text)

	def echo_all(self, message):
		# write_json(message.json, '../message.json')
		self.bot.send_message(message.chat.id, message.text,
							  reply_markup=keyboards.main
							  )

if __name__=='__main__':
	logger.info('Bot started')
	bot = Bot()
	bot.run()