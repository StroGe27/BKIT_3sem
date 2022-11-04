# -*- coding: cp1251 -*-
import pytest
from RK_2 import Example_1
from RK_2 import Example_2
from RK_2 import Example_3
from RK_2 import one_to_many

#�������� �� �������� ��� �������� ������

def test_result_example_1():
    temp = Example_1(one_to_many)  

    assert temp[0] == ('�������', 450, 'OOO."��� �������"', 50)
    assert temp[1] == ('�������', 350, 'OOO."��� �������"', 60)
    assert temp[2] == ('����', 250, 'OOO."���� � ������"', 300)
    assert temp[3] == ('�������', 375, 'OOO."���� � ������"', 200)
    assert temp[4] == ('������', 500, '��."���� � �������"', 100)

def test_result_example_2():
    temp = Example_2(one_to_many)  

    assert temp[0] == ('OOO."���� � ������"', 150000)
    assert temp[1] == ('��."���� � �������"', 50000)
    assert temp[2] == ('OOO."��� �������"', 43500)

def test_result_example_3():
    temp = Example_3(one_to_many)

    assert temp == {'OOO."���� � ������"': ['����', '�������'], 'OOO."��� �������"': ['�������', '�������']}