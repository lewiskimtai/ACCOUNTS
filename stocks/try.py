stock = []
class Stocks:

    
    def __init__(self, product, quantity, buying_price, selling_price):
        self.product = product
        self.quantity = quantity
        self.buying_price = buying_price
        self.selling_price = selling_price

w = input('Enter your name:')
x = input('Enter your name:')
y = input('Enter your name:')
z = input('Enter your name:')



iphone = Stocks(w, x, y, z)
tecno = Stocks('tecno', '5', '500', '1000')
stock.append(iphone)
#stock.append(tecno)
print(Stocks)
for x in stock:
  print(x.product)

  


