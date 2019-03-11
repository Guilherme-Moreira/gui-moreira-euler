def checkPandigital(n):
    hash = {}
    for char in '123456789':
        hash[char] = 0

    for digit in str(n):
        try:
            hash[digit] += 1
        except KeyError:
            return False
    for key, value in hash.items():
        if value != 1:
            return False

    return True


larg = 0
i = 1
while True:
    d = str(i)
    cur = 2
    while len(d) < 9:
        d = d + str(i * cur)
    if checkPandigital(int(d)):
        if int(d) > larg:
            larg = int(d)
            print(larg)  # eventually prints 932718654
    i += 1
