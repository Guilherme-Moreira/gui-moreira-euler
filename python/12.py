import math


def triang():
    i = 2
    while True:
        n = 0
        for j in range(i):
            n += j

        yield n
        i += 1


def countDivisors(n):
    divs = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            divs += 1

    return divs * 2


for item in triang():
    if countDivisors(item) > 500:
        print(item)  # 76576500
        break
