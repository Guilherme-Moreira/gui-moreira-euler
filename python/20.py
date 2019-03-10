import math


s = 0
n = str(math.factorial(100))
for digit in n:
    s += int(digit)

print(s)  # 548
