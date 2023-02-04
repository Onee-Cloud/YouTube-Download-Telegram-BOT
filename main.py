import config
import pytube
import telebot

from pytube import YouTube
from telebot import types

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, config.GREETING[0])
    bot.send_message(message.chat.id, config.GREETING[1])

@bot.message_handler(content_types=['text'])
def start_message(message):
    if ('youtube.com' in message.text) or ('youtu.be' in message.text):
        video = None
        try:
            video = YouTube(message.text)
        except Exception:
            bot.send_message(message.chat.id, 'Помилка, перевірте посилання та  спробуйте ще')
        finally:
            bot.send_message(message.chat.id, 'Назва відео: {title} \n Кількість переглядів: {views} \n Довжина відео: {length}'.format(title=video.title, views=video.views, length=str(video.length//60) + ' : ' + str(video.length%60)))
            ys = video.streams.get_highest_resolution()
            bot.send_message(message.chat.id, 'Завантаження почалось зачекайте будьласка')
            ys.download(None, 'video.mp4')
            bot.send_message(message.chat.id, 'Завантаження закінчилось відправляємо вам')
            vid = open('video.mp4', 'rb')
            bot.send_video(message.chat.id, vid)
            vid.close()




bot.polling(none_stop = True)