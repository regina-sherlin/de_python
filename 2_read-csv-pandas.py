import pandas as pd

df = pd.read_csv('orders-ex1.csv')
print(df)
total = df['amount'].sum()
print(round(total, 2))