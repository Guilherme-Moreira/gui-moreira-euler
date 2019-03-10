import math


def isPrime(n):
    prime = True
    if n < 0:
        n *= -1
    if n >= 2:
        for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
            if n % i == 0:
                prime = False
    elif n != 1:
        prime = True
    return prime


maxA, maxB, maxS = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        x = 0
        exp = x ** 2 + a * x + b
        while True:
            if isPrime(exp):
                x += 1
                exp = x ** 2 + a * x + b
            else:
                break
        if x > maxS:
            maxS, maxA, maxB = x, a, b

print(maxA * maxB)  # -59231
