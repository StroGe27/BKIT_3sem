def sort_array(data, temp):
    #data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    if temp == 1:
        result = sorted(data, key = abs)[::-1]
        print(result)
    elif temp == 2:
        result_with_lambda = sorted(data, key = lambda x: abs(x))[::-1]
        print(result_with_lambda)
    else:
        print("ERROR")