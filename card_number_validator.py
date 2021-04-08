from cipher_check_16 import cipher_check_16

def card_number_validator(card_number):
    card_number_list = cipher_check_16(int(card_number))

    odd_index = []
    even_index = []
    for o in range(0,8):
        odd_index.append(o * 2)
    for e in range(0,8):
        even_index.append(e * 2 + 1)

    odd_number = []
    even_number = []
    for n in odd_index:
        temp = card_number_list[n] * 2
        if temp >= 10:
            odd_number.append(temp % 10 + 1)
        else:
            odd_number.append(temp)
    for n in even_index:
        even_number.append(card_number_list[n])

    odd_total = sum(odd_number)
    even_total = sum(even_number)

    total = odd_total + even_total

    if total % 10 == 0:
        return 1
    else:
        return 0
