import math


def isPrime(n):
    prime = True
    if n >= 2:
        for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
            if n % i == 0:
                prime = False
    elif n != 1:
        prime = True
    return prime


nPrimes = 0
i = 0
while nPrimes <= 10001:
    if isPrime(i):
        nPrimes += 1

    i += 1

print(i-1)  # 104743
