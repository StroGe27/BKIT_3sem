# -*- coding: cp1251 -*-
from operator import itemgetter
class Detail: #Emp
    #Деталь
    def __init__(self, id, name, cost, count_det, det_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.det_id = det_id
        self.count = count_det
 
class Provider: #Dep
    #Поставщик
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class DetProv: #DetProv
    #'Поставляемые поставщиком детали' для реализации связи многие-ко-многим
    def __init__(self, dep_id, det_id):
        self.dep_id = dep_id
        self.det_id = det_id

# Поставщики
Providers = [
    Provider(1, 'OOO."Рога и копыта"'),
    Provider(2, 'OOO."Моя оборона"'),
    Provider(3, 'ИП."Рога и подковы"'),
]
 
# Детали
Details = [
    Detail(1, "Болт", 250, 300, 1),
    Detail(2, "Саморез", 375, 200, 1),

    Detail(3, "Вкладыш", 450, 50, 2),
    Detail(4, "Бобышка", 350, 60, 2),
    
    Detail(5, "Штуцер", 500, 100, 3),
]
 
# Связи
Detail_Provider = [
    DetProv(1,1),
    DetProv(2,2),
    DetProv(3,3),
]
 
def main():
    # Соединение данных один-ко-многим 
    one_to_many = [(e.name, e.cost, d.name, e.count) 
        for d in Providers 
        for e in Details 
        if e.det_id == d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.dep_id, ed.det_id) 
        for d in Providers 
        for ed in Detail_Provider 
        if d.id == ed.dep_id]
    
    many_to_many = [(e.name, e.cost, dep_name) 
        for dep_name, dep_id, det_id in many_to_many_temp
        for e in Details if e.id == det_id]
 
    print('Example A1')
    res_11 = sorted(one_to_many, key = itemgetter(2))
    print(res_11)

    print('\nExample A2')
    res_12_unsorted = []
    # Перебираем всех поставщиков
    for d in Providers:
        # Список деталей поставщиков
        d_details = list(filter(lambda i: i[2] == d.name, one_to_many))        
        if len(d_details) > 0:
            # Стоимоть деталей у постащика
            d_sals = [cost*count for _,cost,_,count in d_details]
            # Суммарная стоимость деталей у поставщика
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))
    # Сортировка по стоимости имеющихся деталей
    res_12 = sorted(res_12_unsorted, key = itemgetter(1), reverse = True)
    print(res_12)
 
    print('\nExample A3')
    res_13 = {}
    # Перебираем всех поставщиков (будем проверять наличие слова: "Рога в названии")
    for d in Providers:
        if 'ООО.' in d.name:
            d_detailz = list(filter(lambda i: i[2] == d.name, one_to_many))   
            if len(d_detailz) > 0:
                # Только название деталей
                d_detailz_names = [x for x,_,_,_ in d_detailz]
                # Добавляем результат в словарь
                # ключ - поставщик, значение - список деталей
                res_13[d.name] = d_detailz_names
    print(res_13)
 
if __name__ == '__main__':
    main()
