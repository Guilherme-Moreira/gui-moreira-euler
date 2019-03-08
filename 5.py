n = 0
while 1:

    n += 20

    for i in range(1, 21):
        if n % i:
            break
    else:
        print(n)  # 232792560
        break
