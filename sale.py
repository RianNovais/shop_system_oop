from datetime import datetime
class Sale():
    def __init__(self, customer,product,quantity):
        self.saleDate = datetime.now().strftime('%d/%m/%Y:%H:%M')
        self.customer = customer
        self.product = product
        self.quantity = quantity




