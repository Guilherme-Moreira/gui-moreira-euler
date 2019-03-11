with open('22.txt') as f:
    data = f.read()

data = data.split('","')
data[0] = data[0][1:]
data[-1] = data[-1][:-1]

data = sorted(data)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0

for index, name in enumerate(data):
    cur = 0
    for char in name:
        cur += alphabet.index(char) + 1
    total += cur * (index + 1)

print(total)  # 871198282
