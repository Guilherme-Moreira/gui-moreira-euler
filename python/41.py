def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def checkPandigital(n, b):
    d = {}
    for i in range(1, b + 1):
        d[i] = 0

    for char in str(n):
        try:
            d[int(char)] += 1
        except KeyError:
            return False

    for key in d:
        if d[key] != 1:
            return False

    return True


a = gen_primes()
while True:
    x = next(a)
    if checkPandigital(x, len(str(x))):
        print(x)

# outputs a long list of numbers, but eventually reaches 7652413 and stops
