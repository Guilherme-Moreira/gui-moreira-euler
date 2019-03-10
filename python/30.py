i = 2
s = 0
while True:
    aval = 0
    for char in str(i):
        aval += int(char) ** 5
    if aval == i:
        s += i
        print(s)  # 4150, 8301, 63049, 155776, 248860, 443839
    i += 1
