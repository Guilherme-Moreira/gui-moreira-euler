def func1(n):
    a, b = 1, 1
    s = 0
    while a < n:
        s += a if a % 2 == 0 else 0
        a, b = b, a+b

    return s


print(func1(4000000))  # 4613732
