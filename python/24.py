import itertools

i = list(itertools.permutations('0123456789'))
print(''.join(i[999999]))  # 2783915460
