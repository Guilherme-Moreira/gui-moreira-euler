a, b = 0, 0

for i in range(1, 101):
    a += i
    b = b + i ** 2

a = a ** 2
print(a - b)  # 25164150
