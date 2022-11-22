# -*- coding: cp1251 -*-
#from pprint import pprint
from config import tg_bot_token
from config import open_weather_token

import requests
import telebot
from telebot import types

bot = telebot.TeleBot(tg_bot_token)

@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Здравствуй, <b>{message.from_user.first_name}, чтобы вывести информацию о температуре в городе, введите название города</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands = ['buttons'])
def mess_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
    city_Moscow = types.KeyboardButton('Moscow')
    city_Peter = types.KeyboardButton('Гитхаб автора')
    markup.add(city_Moscow, city_Peter)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup = markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)

@bot.message_handler(content_types = 'text')
def mess_weather(message):
    city = message.text.lower()
    data = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&limit={}&appid={}".format(city, 1, open_weather_token)).json()
    if data == []:
        if city == "гитхаб автора":
            bot.send_message(message.chat.id, "https://github.com/StroGe27?tab=repositories")
        else:
            bot.send_message(message.chat.id, "Проверьте название города")
    else:
        r_info = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&lang=ru&units=metric".format(data[0]["lat"], data[0]["lon"], open_weather_token)).json()

        city = r_info["name"] # название города
        weather_temp = r_info["main"]["temp"] # температура
        weather_humidity = r_info["main"]["humidity"] # влажность
        weather_pressure = r_info["main"]["pressure"] # давление
        weather_wind = r_info["wind"]["speed"] # скорость ветра
        weather_description = r_info["weather"][0]["description"] # название погоды
        weather_icon = str(r_info["weather"][0]["icon"]) # иконка погоды

        photo = open('weather_photo\{}@2x.png'.format(weather_icon), 'rb')
        bot.send_photo(message.chat.id, photo, caption = f"Погода в городе: {city} - {weather_description}\nТемпература: {weather_temp}°C\nВлажность: {weather_humidity}\nДавление: {weather_pressure}\nСкорость ветра: {weather_wind}")

        #pprint(r_info)

bot.polling(none_stop = True)