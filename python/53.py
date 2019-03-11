from operator import mul
from fractions import Fraction


def nCr(n, r):
    return int(reduce(mul, (Fraction(n-i, i+1) for i in range(r)), 1))  # https://stackoverflow.com/questions/3025162/statistics-combinations-in-python/3027128


answ = 0

for n in range(1, 101):
    for r in range(1, n+1):
        if nCr(n, r) > 1000000:
            answ += 1

print(answ)  # 4075
