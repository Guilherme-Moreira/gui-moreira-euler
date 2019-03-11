def lychrel(n):
    iterations = 1
    n = n + int(str(n)[::-1])
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        iterations += 1
        if iterations >= 50:
            return 1

    return 0


n = 0
for i in range(1, 10000):
    n += lychrel(i)

print(n)  # 249
