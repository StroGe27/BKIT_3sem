#import asyncio
#import time

#���������� openweather
import requests
from config import open_weather_token


import telebot
from telebot import types
bot = telebot.TeleBot('5390890783:AAHgTuMn3jqD-yb8H5xc3uU0k7-C_krfQqU')


def get_weather(city, open_weather_token):
    try:
    except Exception as ex:
        print(ex)
        print("��������� �������� ������")

def main():
    city =input("������� �����")
    get_weather(city, open_weather_token)
if __name__ == "__main__":
    main()