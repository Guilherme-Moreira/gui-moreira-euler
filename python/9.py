for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if c ** 2 == a ** 2 + b ** 2 and a+b+c == 1000:
                print(a*b*c)  # 31875000
                break
