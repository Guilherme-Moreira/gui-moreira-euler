# this is such a convoluted method, but it works ¯\_(ツ)_/¯

date = [1, 1, 1900]

month30 = [4, 6, 9, 11]
month31 = [1, 3, 5, 7, 8, 10, 12]

week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
weekDay = 0

ans = 0

while date[2] < 2001:

    weekDay = weekDay + 1 if weekDay < 6 else 0

    if date[1] in month30:
        date[0] = date[0] + 1 if date[0] < 30 else 1

    elif date[1] in month31:
        date[0] = date[0] + 1 if date[0] < 31 else 1

    else:
        if date[2] % 100 == 0 and date[2] % 400 == 0:
            date[0] = date[0] + 1 if date[0] < 29 else 1
        elif date[2] % 4 == 0:
            date[0] = date[0] + 1 if date[0] < 29 else 1
        else:
            date[0] = date[0] + 1 if date[0] < 28 else 1

    if date[0] == 1:
        if date[1] == 12:
            date[1] = 1
            date[2] += 1
        else:
            date[1] += 1

    if date[2] >= 1901 and date[2] < 2001:
        if week[weekDay] == 'sun' and date[0] == 1:
            ans += 1


print(ans)  # 171
