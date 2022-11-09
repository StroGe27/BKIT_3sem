# -*- coding: cp1251 -*-
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort_array
from lab_python_fp.print_result import print_result_tests
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
import time
def main():
    print("Example 1")
    goods = [
    {'title': 'Kover', 'price': 2000, 'color': 'green'},
    {'title': 'Divan dlia otdiha', 'color': 'black'}
    ]
    print(*field(goods, 'title'))
    print(*field(goods, 'title', 'price'))

    print("Example 2")
    gen_random(5, 1, 3)

    print("Example 3")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(Unique(data))
    data = gen_random(10, 1, 3)
    print(Unique(data))
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(Unique(data))
    print(Unique(data, ignore_case = True))

    print("Example 4")
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    sort_array(data, 1)
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    sort_array(data, 2)
    
    print("Example 5")
    print_result_tests()
    
    print("Example 6")
    with cm_timer_2():
       time.sleep(1.5)
    with cm_timer_2():
        time.sleep(5.5)
    

if __name__ == "__main__":
    main()
