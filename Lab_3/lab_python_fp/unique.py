from xml.etree.ElementTree import tostring


class Unique(object):
    def __init__(self, items, **kwargs):
        pass
    def __init__(self, args, ignore_case = False):
        self.args_obj = set(args)
        # ����� ����������� �����������
        # � �������� ��������� ���������, ����������� ������ ��������� bool-�������� ignore_case,
        # � ����������� �� �������� �������� ����� ��������� ����������� ������ � ������ ��������
        # ��������: ignore_case = True, A�� � ��� - ������ ������
        #           ignore_case = False, A�� � ��� - ���������� ������, ���� �� ������� ��������
        # ��-��������� ignore_case = False
    def __str__(self):
        temp = tostring(self.args_obj)
        return temp
    def __next__(self):
        # ����� ����������� __next__    
        pass

    def __iter__(self):
        return self