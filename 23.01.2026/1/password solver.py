import random
for  in range(100):
    while True:
        lenght = random.randint(8, 16)
        num = [random.randint(33, 126) for  in range(lenght - 1)]

        result = (lenght * 80) - sum(num)

        if 33 <= result <= 126:
            print("".join(map(chr, num + [result])))
            break