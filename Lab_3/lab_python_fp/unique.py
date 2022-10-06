from xml.etree.ElementTree import tostring


class Unique(object):
    def __init__(self, items, **kwargs):
        pass
    def __init__(self, args, ignore_case = False):
        self.args_obj = set(args)
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
    def __str__(self):
        temp = tostring(self.args_obj)
        return temp
    def __next__(self):
        # Нужно реализовать __next__    
        pass

    def __iter__(self):
        return self