i = 1
while True:
    for j in range(2, 7):
        if sorted(str(i)) != sorted(str(i*j)):
            break
    else:
        print(i)  # 142857
        break
    i += 1
