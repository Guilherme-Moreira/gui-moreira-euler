import math


def gen_triang():
    i = 1
    while True:
        yield i*(i+1)//2
        i += 1


def check_h(n):
    x = ((math.sqrt(8*n + 1) + 1)/4)
    if int(x) == x:
        return True
    return False


def check_p(n):
    x = ((math.sqrt(24*n + 1) + 1)/6)
    if int(x) == x:
        return True
    return False


a = gen_triang()
while True:
    i = next(a)
    if check_h(i) and check_p(i) and i > 40755:
        print(i)  #  1533776805
        break
