class Unique(object):
    def __init__(self, items, **kwargs):
        self.__r = []
        if kwargs == {}:
            try:
                self.__r = sorted(set([i for i in items]))
            finally:
                return

        for key, value in kwargs.items():
            if key == "ignore_case" and value == True:
                try:
                    self.__r = sorted(set([i.lower() for i in items]))
                finally:
                    break
            
                 
    def unique(self):
        return self.__r
    def __next__(self):
        try:
            temp = self.__r[self.begin]
            self.begin += 1
            return temp
        except:
            raise StopIteration
    def __str__(self):
        return str(self.__r)
    def __iter__(self):
        return self