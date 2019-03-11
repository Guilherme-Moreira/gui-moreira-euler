import itertools


a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b = list(itertools.permutations(a))

s = 0


for perm in b:
    cur = ''.join(perm)
    condA = int(cur[1:4]) % 2
    condB = int(cur[2:5]) % 3
    condC = int(cur[3:6]) % 5
    condD = int(cur[4:7]) % 7
    condE = int(cur[5:8]) % 11
    condF = int(cur[6:9]) % 13
    condG = int(cur[7:10]) % 17

    # Super ugly solution, but works

    if condA == 0 and condB == 0 and condC == 0 and condD == 0 and condE == 0 and condF == 0 and condG == 0:
        s += int(cur)


print(s)  # 16695334890
