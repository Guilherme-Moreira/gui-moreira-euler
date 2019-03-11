import math

lines = [line.strip('\n') for line in open('99.txt')]

maxValue = 0
line = 0
maxLine = 1

for value in lines:
    line += 1
    values = value.split(',')
    val1, val2 = int(values[0]), int(values[1])
    ans = val2 * math.log(val1)
    if ans > maxValue:
        maxValue = ans
        maxLine = line
        print(maxValue, maxLine)
