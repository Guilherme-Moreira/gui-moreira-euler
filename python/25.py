def fibonnaci():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


a = fibonnaci()
i = 1
while True:
    if len(str(next(a))) >= 1000:
        print(i)  # 4782
        break
    i += 1
