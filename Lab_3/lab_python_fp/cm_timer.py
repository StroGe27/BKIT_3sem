from contextlib import contextmanager
import time
class cm_timer_1:
    def __enter__(self):
        self.__time_begin = time.time()
    def __exit__(self, type, value, traceback):
        print(time.time() - self.__time_begin)

@contextmanager
def cm_timer_2():
    time_begin = time.time()
    yield 
    print(time.time() - time_begin)