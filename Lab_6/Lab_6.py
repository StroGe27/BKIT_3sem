# -*- coding: cp1251 -*-
import requests
from pprint import pprint
from config import open_weather_token

#Доделать нормальный вывод данных

def get_weather(city):
    try:
        data = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&limit={}&appid={}".format(city, 5, open_weather_token)).json()
        print("---------------------------------------------------------")
        r_info = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(data[0]["lat"], data[0]["lon"], open_weather_token)).json()
        pprint(r_info)
        print("---------------------------------------------------------")
        city = r_info["name"]
        weather_temp = r_info["main"]["temp"] # температура
        weather_humidity = r_info["main"]["humidity"] # влажность
        weather_pressure = r_info["main"]["pressure"] # давление
        weather_wind = r_info["wind"]["speed"] # скорость ветра
        #weather_...
        print(f"Погода в городе: {city}\nТемпература: {weather_temp}\nВлажность: {weather_humidity}\nДавление: {weather_pressure}\nСкорость ветра: {weather_wind}")
    except Exception as ex:
        print(ex, "Проверьте название города")