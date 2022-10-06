from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort_array
from lab_python_fp.print_result import print_result_tests
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
import time
def main():
    goods = [
    {'title': 'Kover', 'price': 2000, 'color': 'green'},
    {'title': 'Divan dlia otdiha', 'color': 'black'}
    ]
    #field(goods, 'title')
    #field(goods, 'title', 'price')
    #gen_random(5, 1, 3)
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    #data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    #print(Unique(data))
    #sort_array(data)
    #print_result_tests()
    with cm_timer_1():
        time.sleep(5.5)
    with cm_timer_2():
        time.sleep(5.5)


if __name__ == "__main__":
    main()
#не сделано:
#3
#6
#7