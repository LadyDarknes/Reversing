import random
for _ in range(100):
    while True:
        lenght = random.randint(8, 16)
        num = [random.randint(65, 90) for _ in range(lenght - 1)]
        
        result = 1240 - sum(num)
        
        if 41 <= result <= 90:
            print("".join(map(chr, num + [result])))
            break
