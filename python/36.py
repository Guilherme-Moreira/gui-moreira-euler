s = 0
for i in range(1000000):
    b = bin(i)[2:]
    if str(i) == str(i)[::-1] and b == b[::-1]:
        s += i

print(s)  # 872187
