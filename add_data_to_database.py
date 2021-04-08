import pandas as pd
import random
import time

# df = pd.read_csv("./database/database.csv", index_col=0)
#
# new_data = {"user_name":"NaKyoung Lee", "card_number":"1111222233334444", "timestamp":"04/08/21", "cvc":"124"}
#
# df = df.append(new_data, ignore_index=True)
# df.to_csv("./database/database.csv")

def add_data_to_database(user_name="", card_number=""):
    df = pd.read_csv("./database/database.csv", index_col=0)

    current_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))

    cvc = ""
    for i in range(0,3):
        cvc += str(random.randint(0, 9))

    new_data = {"user_name": user_name, "card_number": card_number,"timestamp": current_time, "cvc": cvc}

    df = df.append(new_data, ignore_index=True)
    df.to_csv("./database/database.csv")