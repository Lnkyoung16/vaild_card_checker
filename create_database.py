import pandas as pd

df = pd.DataFrame([], columns=["user_name", "card_number", "cvc", "timestamp"])
df.to_csv("./database/database.csv")