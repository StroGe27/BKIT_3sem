# -*- coding: cp1251 -*-
import requests
from pprint import pprint
from config import open_weather_token

#�������� ���������� ����� ������

def get_weather(city):
    try:
        data = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&limit={}&appid={}".format(city, 5, open_weather_token)).json()
        print("---------------------------------------------------------")
        r_info = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(data[0]["lat"], data[0]["lon"], open_weather_token)).json()
        pprint(r_info)
        print("---------------------------------------------------------")
        city = r_info["name"]
        weather_temp = r_info["main"]["temp"] # �����������
        weather_humidity = r_info["main"]["humidity"] # ���������
        weather_pressure = r_info["main"]["pressure"] # ��������
        weather_wind = r_info["wind"]["speed"] # �������� �����
        #weather_...
        print(f"������ � ������: {city}\n�����������: {weather_temp}\n���������: {weather_humidity}\n��������: {weather_pressure}\n�������� �����: {weather_wind}")
    except Exception as ex:
        print(ex, "��������� �������� ������")