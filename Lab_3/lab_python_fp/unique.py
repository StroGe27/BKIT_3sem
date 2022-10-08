class Unique(object):
    def __init__(self, items, **kwargs):
        self.__r = []
        for key, value in kwargs.items():
            if key == "ignore_case" and value == True:
                try:
                    items = [i.lower() for i in items]
                finally:
                    break
        print(*sorted(set(items)), sep = ", ")

    def __next__(self):
        try:
            temp = self.__r[self.begin]
            self.begin += 1
            return temp
        except:
            raise StopIteration

    def __iter__(self):
        return self