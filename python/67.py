from time import time

with open('67.txt') as f:
    triangle = f.read()

start = time()

triangle = triangle.split('\n')
triangle = [[int(x) for x in row.split(' ') if x != ''] for row in triangle]
triangle.reverse()


previousLine = []
for row in triangle:
    current = []
    if previousLine == []:
        for char in row:
            current.append(char)
    else:
        for index in range(len(row)):
            buf = [previousLine[index], previousLine[index + 1]]
            valueToAdd = max(buf)
            current.append(valueToAdd + row[index])
    previousLine = current
print(current[0])  # 7273
print(time() - start)
