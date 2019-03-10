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


a = gen_primes()
s = 0
for item in a:
    if item < 2000000:
        s += item
    else:
        break

print(s)  # 142913828922
