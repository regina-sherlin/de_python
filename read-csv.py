import csv

with open('orders-ex1.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    total=0
    for row in reader:
        if row['amount']:
            total += float(row['amount'])
    print(round(total, 2))