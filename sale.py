from datetime import datetime

# this class is a sales class, it receives a customer, a product, and the quantity to be sold, it is instantiated in
# the "make sale" method defined in shop

class Sale():


    def __init__(self, customer,product,quantity):
        self.saleDate = datetime.now().strftime('%d/%m/%Y:%H:%M')
        self.customer = customer
        self.product = product
        self.quantity = quantity




