import json
import sys
#from lab_python_fp.field import field
#from lab_python_fp.gen_random import gen_random
#from lab_python_fp.unique import Unique
#from sort import sort_array
from print_result import print_result
from cm_timer import cm_timer_1, cm_timer_2
import time
# ������� ������ ����������� �������

path = None

# ���������� � ���������� path ��������� ���� � �����, ������� ��� ������� ��� ������� ��������

with open("D:\pp\BKIT_3sem\BKIT_3sem\Lab_3\lab_python_fp\data_light.json") as f:
    data = json.load(f)

# ����� ���������� ����������� ��� ������� �� �������, ������� `raise NotImplemented`
# ��������������, ��� ������� f1, f2, f3 ����� ����������� � ���� ������
# � ���������� ������� f4 ����� ���� �� 3 �����

@print_result
def f1(arg):
    pass


@print_result
def f2(arg):
    pass


@print_result
def f3(arg):
    pass


@print_result
def f4(arg):
    pass


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))