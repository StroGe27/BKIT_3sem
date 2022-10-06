def sort_array(data):
    #data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    result = sorted(data, key = abs)[::-1]
    print(result)
    result_with_lambda = sorted(data, key = lambda x: abs(x))[::-1]
    print(result_with_lambda)