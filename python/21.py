import math


def sumOfDivisors(n):
    s = 1
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            s += i
            s += n / i

    return s


answ = 0
for i in range(1, 10000):
    j = sumOfDivisors(i)
    if sumOfDivisors(j) == i and i != j:
        answ += i

print(answ)  # 31626
