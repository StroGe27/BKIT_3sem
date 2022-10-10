from contextlib import contextmanager
from time import time
class cm_timer_1:
    def __enter__(self):
        self.__time_begin = time()
    def __exit__(self, type, value, traceback):
        print(time() - self.__time_begin)

@contextmanager
def cm_timer_2():
    time_begin = time()
    yield 
    print(time() - time_begin)