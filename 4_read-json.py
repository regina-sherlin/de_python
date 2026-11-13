import json

with open('orders.json', encoding='utf-8') as file:
    data = json.load(file)

print(data['data'][2]['customer']['city'])
print(data['data'][0]['items'][1]['sku'])
print(data['data'][1]['amount'])

#total of amounts in nested json
total=0
for order in data['data']:
    amount=order.get('amount')
    if amount is not None:
        total +=amount 
print(total)


# loop customers state
for order in data['data']:
    state=order.get('customer', {}).get('state')
    print(state)


# loop customer name of paid customers.
for order in data['data']:
    if order.get('paid'):
        print(order.get('customer').get('name'))


# print every order id one per line 
for order in data['data']:
    orderid=order.get('order_id')
    print(orderid)


# print names of customers whose state is tn 
for order in data['data']:
    state=order.get('customer',{}).get('state')
    if state == 'TN':
        print(order.get('customer',{}).get('name'))


# print order id and amount for orders with amount > 100
for order in data['data']:
    order_amt = order.get('amount')
    if order_amt is not None and order_amt > 100:
        print(order.get('order_id'), order_amt)


#Count how many orders are not paid, then print the Count
count=0
for order in data['data']:
    order_paid = order.get('paid')
    if not order_paid:
        count+=1
print(count)

#print every sku across all orders 
for order in data['data']:
    for item in order.get('items',{}):
        print(item['sku'])

# print order id of any order that has no items 
for order in data['data']:
    if len(order['items']) ==0:
        print(order.get('order_id'))


#print total qty if items sold across all orders
total_qty=0
for order in data['data']:
    for item in order['items']:
        total_qty+=item['qty']
print(total_qty)


# build a new list containing only {name city } for paid orders then print list
newlist={}
for order in data['data']:
    paid_order = order.get('paid')
    if paid_order:
        newlist['name']=order.get('customer',{}).get('name')
        newlist['city']=order.get('customer',{}).get('city')
        print(newlist)


# find order id with highest amount - skip none amounts
max_amount=0
for order in data['data']:
    order_amount = order.get('amount')
    if order_amount is not None and order_amount > max_amount:
        max_amount = order_amount
        print(order.get('order_id'))


for order in data['data']:
    items_tot=0
    for item in order.get('items'):
        items_tot += (item['qty'] * item['price'])
        items_tot = round(items_tot,2)
    if items_tot == order.get('amount'):
        print(order.get('order_id'), items_tot, order.get('amount'), 'MATCH')
    else:
        print(order.get('order_id'), items_tot, order.get('amount'), 'MISMATCH')