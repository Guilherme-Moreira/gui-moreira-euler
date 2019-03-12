def check(n):
    a = '123456789'
    if ''.join(sorted(str(n))) == a:
        return True
    else:
        return False


i = 1
products = []
s = 0
while True:
    j = 1
    while True:
        if len(str(i * j)) + len(str(j)) + len(str(i)) > 9:
            break
        else:
            if check(str(i) + str(j) + str(i * j)):
                if i * j not in products:
                    products.append(i * j)
                    s += i * j
                    print(s)  # 45228
        j += 1
    i += 1
