#декоратор
def print_result(fun):
    def wrapper():
        print(fun.__name__)
        if isinstance(fun(), list):
            print(*fun(), sep = "\n")
        elif isinstance(fun(), dict):
            temp_fun = fun()
            for i in temp_fun:
                print(i, temp_fun.get(i), sep = " = ")
        else:
            print(fun())
    return wrapper

@print_result
def test_1():   
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

def print_result_tests():
    test_1()
    test_2()
    test_3()
    test_4()