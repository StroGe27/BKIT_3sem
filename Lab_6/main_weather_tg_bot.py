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
    mess = f'����������, <b>{message.from_user.first_name}, ����� ������� ���������� � ����������� � ������, ������� �������� ������</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands = ['buttons'])
def mess_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
    city_Moscow = types.KeyboardButton('Moscow')
    city_Peter = types.KeyboardButton('������ ������')
    markup.add(city_Moscow, city_Peter)
    bot.send_message(message.chat.id, '�������� ��� ��� ����', reply_markup = markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)

@bot.message_handler(content_types = 'text')
def mess_weather(message):
    city = message.text.lower()
    data = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&limit={}&appid={}".format(city, 1, open_weather_token)).json()
    if data == []:
        if city == "������ ������":
            bot.send_message(message.chat.id, "https://github.com/StroGe27?tab=repositories")
        else:
            bot.send_message(message.chat.id, "��������� �������� ������")
    else:
        r_info = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&lang=ru&units=metric".format(data[0]["lat"], data[0]["lon"], open_weather_token)).json()

        city = r_info["name"] # �������� ������
        weather_temp = r_info["main"]["temp"] # �����������
        weather_humidity = r_info["main"]["humidity"] # ���������
        weather_pressure = r_info["main"]["pressure"] # ��������
        weather_wind = r_info["wind"]["speed"] # �������� �����
        weather_description = r_info["weather"][0]["description"] # �������� ������
        weather_icon = str(r_info["weather"][0]["icon"]) # ������ ������

        photo = open('weather_photo\{}@2x.png'.format(weather_icon), 'rb')
        bot.send_photo(message.chat.id, photo, caption = f"������ � ������: {city} - {weather_description}\n�����������: {weather_temp}�C\n���������: {weather_humidity}\n��������: {weather_pressure}\n�������� �����: {weather_wind}")

        #pprint(r_info)

bot.polling(none_stop = True)