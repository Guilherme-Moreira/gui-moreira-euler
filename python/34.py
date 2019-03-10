import math

i = 3
s = 0

while True:
    aval = 0
    for char in str(i):
        aval += math.factorial(int(char))
    if aval == i:
        s += i
        print(s)  # 145, 40730
    i += 1
