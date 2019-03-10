def collatz(n):
    a = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        a += 1
    return a


m = 0
answ = 0
for i in range(1, 1000000):
    if collatz(i) > m:
        m = collatz(i)
        answ = i

print(answ)  # 837799
