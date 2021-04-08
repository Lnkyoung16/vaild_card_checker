import random
from card_number_validator import card_number_validator
from query_card_number import query_card_number
from add_data_to_database import add_data_to_database


def card_number_generator(user_name):
    while True:
        card_number = "2021"

        for i in range(0,12):
            number = str(random.randint(0,9))
            card_number = card_number + number

        if card_number_validator(card_number):
            if query_card_number(card_number) == 0:
                card_number = str(card_number)
                add_data_to_database(user_name, card_number)
                break

card_number_generator("asdf")