from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort_array
from lab_python_fp.print_result import print_result_tests
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
    print_result_tests()


if __name__ == "__main__":
    main()
#�� �������:
#3 - test_3
#5
#6
#7