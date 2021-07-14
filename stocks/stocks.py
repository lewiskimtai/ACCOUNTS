stock = {
  'product': [],
  'quantity': [],
  'buying_price': [],
  'selling_price': []
}

new_product = input('Enter product:')
stock['product'].append(new_product)
print(stock['product'])
print(stock)

quantity = input('Enter quantity:')
stock['quantity'].append(quantity)
print(stock['quantity'])
print(stock)

buying_price = input('Enter product buying price:')
stock['buying_price'].append(buying_price)
print(stock['buying_price'])
print(stock)

selling_price = input('Enter product selling price:')
stock['selling_price'].append(selling_price)
print(stock['selling_price'])
print(stock)


#print(sum(stock['quantity']))
#print(int(sum(stock['price'])))






