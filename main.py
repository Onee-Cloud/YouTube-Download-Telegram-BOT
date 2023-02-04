import config
import pytube
import telebot

from pytube import YouTube
from telebot import types

link = ''

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, config.GREETING[0])
    bot.send_message(message.chat.id, config.GREETING[1])

@bot.message_handler(content_types=['text'])
def start_message(message):
    if 'youtube.com' in message.text:
        try:
            YouTube(message.text)
            bot.send_message(message.chat.id, message.text)
        except Exception:
            bot.send_message(message.chat.id, 'Введіть коректне посилання')



bot.infinity_polling()