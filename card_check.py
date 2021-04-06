from cipher_check_16 import cipher_check_16

card_number = 0

while True:
    card_number = str(input("카드 숫자를 입력하시오:"))
    if len(card_number) == 16:
        card_number = int(card_number)
        break
    else:
        print("16자리의 숫자를 입력해주세요.")

card_number_list = cipher_check_16(card_number)

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
    print("Valid")
else:
    print("Invalid")