def number_input():
    card_number = 0
    while True:
        card_number = str(input("카드 숫자를 입력하시오:"))
        if len(card_number) == 16:
            card_number = int(card_number)
            break
        else:
            print("16자리의 숫자를 입력해주세요.")
    return card_number

