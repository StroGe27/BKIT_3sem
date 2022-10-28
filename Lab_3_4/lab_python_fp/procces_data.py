# -*- coding: cp1251 -*-
import json
from xml.etree.ElementTree import tostring
from field import field
from gen_random import gen_random
from unique import Unique
from sort import sort_array
from print_result import print_result
from cm_timer import cm_timer_1, cm_timer_2

from operator import concat

def f1(data):
    return Unique(field(data, 'job-name'), ignore_case = True).unique()

def f2(temp):
    return filter(lambda a: a.startswith('�����������'), temp)

def f3(temp):
    return list(map(lambda x: concat(x, ' c ������ Python'), temp))

def f4(temp):
    return zip(temp, gen_random(len(temp), 100000, 200000))

if __name__ == '__main__':    
    with open('lab_python_fp\data_light.json', encoding = "UTF-8-sig") as f:
        data = json.load(f)
    with cm_timer_1():
        for i in f4(f3(f2(f1(data)))):  
            print(i)