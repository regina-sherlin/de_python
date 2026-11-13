import pandas as pd

df = pd.read_csv('messy_orders.csv', dtype={' Order ID': str}, na_values=['-'])

# Clean column names 
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
print(list(df.columns))

# Sum of all amounts 
print(df['amount'].sum())

# Change date type 
df['order_date'] = pd.to_datetime(df['order_date'], format='%d/%m/%Y')
print(df.dtypes)

print(df)

# split city and state into separate columns
df[['city', 'state']] = df['city'].str.split(',', expand=True)
df['city'] = df['city'].str.strip()
df['state'] = df['state'].str.strip()

print(df)