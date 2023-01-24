# the order.py contains a constructor to create our order object, 
# takes in string and numerical values from the runner / controller

class Order:
   # The __init__ should contain all of the values needed for your order object
   def __init__(self, customer_name, drink_size, extras, price):
      self.customer_name = customer_name
      self.drink_size = drink_size
      self.extras = extras
      self.price = price

   def create_order_objects(self):
      print('customer: ' + self.customer_name + ', drink size: ' + self.drink_size + ', extras: ' + self.extras + ', price: ' + str(self.price))
   
order1 = Order('John', 'Small', 'Marshmallows', 3.70)
order1.create_order_objects()