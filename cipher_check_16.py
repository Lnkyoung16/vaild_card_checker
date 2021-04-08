def cipher_check_16(x):
    cipher = []
    result = []
    for z in range(0, 16):
        cipher.append(10**(15 - z))
        temp = 0
    for c in cipher:
        temp = x / c
        temp = int(temp)
        result.append(temp)
        x = x - (temp * c)
    return result