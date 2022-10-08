import random
def gen_random(num_count, begin, end):
    assert num_count > 0
    temp = []
    for i in range(num_count):
        temp.append(random.randrange(begin, end + 1))
    print(*temp, sep = ", ")
    return temp