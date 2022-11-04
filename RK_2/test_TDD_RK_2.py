# -*- coding: cp1251 -*-
import pytest
from RK_2 import Example_1
from RK_2 import Example_2
from RK_2 import Example_3
from RK_2 import one_to_many

#Разделил на элементы для удобства чтения

def test_result_example_1():
    temp = Example_1(one_to_many)  

    assert temp[0] == ('Вкладыш', 450, 'OOO."Моя оборона"', 50)
    assert temp[1] == ('Бобышка', 350, 'OOO."Моя оборона"', 60)
    assert temp[2] == ('Болт', 250, 'OOO."Рога и копыта"', 300)
    assert temp[3] == ('Саморез', 375, 'OOO."Рога и копыта"', 200)
    assert temp[4] == ('Штуцер', 500, 'ИП."Рога и подковы"', 100)

def test_result_example_2():
    temp = Example_2(one_to_many)  

    assert temp[0] == ('OOO."Рога и копыта"', 150000)
    assert temp[1] == ('ИП."Рога и подковы"', 50000)
    assert temp[2] == ('OOO."Моя оборона"', 43500)

def test_result_example_3():
    temp = Example_3(one_to_many)

    assert temp == {'OOO."Рога и копыта"': ['Болт', 'Саморез'], 'OOO."Моя оборона"': ['Вкладыш', 'Бобышка']}