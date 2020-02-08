#!/usr/bin/env python
import os
import sys
import telebot
import time
from StravaPythonClient import swagger_client
from StravaPythonClient.swagger_client.rest import ApiException


swagger_client.configuration.access_token = '08645941baeab0766c359d09e1070320540e7f95'
bot = telebot.TeleBot('1005059602:AAGTsntwFkEe6D89Msb8lmWVUvGDxzuuVrA')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет, хочу тренироваться', 'Пока')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Я знаю, что хочу бегать', 'Я не знаю, что хочу бегать', 'Пока')
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('Моя статисктика', 'Пока')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

api_instance = swagger_client.AthletesApi()
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет, хочу тренироваться':
        name = message.from_user.first_name
        bot.send_message(message.chat.id, ['Привет, ' + name + ', тогда начнем!'], reply_markup=keyboard2)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я знаю, что хочу бегать':
        bot.send_message(message.chat.id, 'Выбери тип соревнования', reply_markup=keyboard3)
    elif message.text.lower() == 'моя статистика':		
        api_response = api_instance.getLoggedInAthlete()
        bot.send_message(message.chat.id,api_response)

bot.polling()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)




