with open("59.txt") as f:
    data = f.read()


data = data.split(',')

alphabet = 'abcdefghijklmnopqrstuvwxyz'


for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            correctKey = False
            key = a + b + c
            message = []
            for index, letter in enumerate(data):
                message.append(chr(ord(key[index % 3]) ^ int(letter)))
            message = ''.join(message).split(' ')
            for word in message:
                if word == 'likewise':  # found this word while printing all messages containing one of the following wors: the, or, The, I, you
                    correctKey = True
            if correctKey is True:
                message = ' '.join(message)
                total = 0
                for char in message:
                    total += ord(char)

                print(total)  # 129448
                break
        if correctKey:
            break
    if correctKey:
        break
