maxS = 0

for a in range(1, 100):
    for b in range(1, 100):
        c = a ** b
        s = 0
        for char in str(c):
            s += int(char)

        if s > maxS:
            maxS = s

print(maxS)  # 972
