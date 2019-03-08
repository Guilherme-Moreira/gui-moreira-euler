def func1(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i

    return s


print(func1(1000))  # 233168
