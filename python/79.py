with open('79.txt') as f:
    data = f.read().split('\n')

data = [char for char in data if char != '']

order = {key: [] for key in range(10)}

for attempt in data:
    for index, digit in enumerate(attempt):
        followingDigits = attempt[index + 1:]
        for n in followingDigits:
            if int(n) not in order[int(digit)]:
                order[int(digit)].append(int(n))

new = {}
for key in order:
    if len(order[key]) != 0:
        new[key] = order[key]


s = sorted(new.items(), key=lambda x: len(x[1]), reverse=True)

password = []
for key in s:
    password.append(str(key[0]))

print(''.join(password) + '0')  # 73162890
