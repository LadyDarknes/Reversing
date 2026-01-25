def sol32bit(val, count):
    return ((val << count) | (val >> (32 - count))) & 0xFFFFFFFF

def keygen(name, salt):
    ebx = 0x97829737 
    multiplier = 0x5BD1E995
    for char in name:
        
        ebx = (ebx ^ ord(char)) & 0xFFFFFFFF
        ebx = (ebx * multiplier) & 0xFFFFFFFF
        ebx = sol32bit(ebx, 5)

        # xor ebx, [ebp+arg_4]
        ebx = (ebx ^ salt) & 0xFFFFFFFF
        
    return ebx

def serial(name):
    part1 = keygen(name, 0x55AA55AA)
    part2 = keygen(name, part1)
    
    return f"{part1:08X}-{part2:08X}"

Nameser = input("Enter name: ")

print(f"Serial: {serial(Nameser)}")