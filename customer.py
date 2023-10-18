from itertools import count
from datetime import datetime

c = count(start=1)

class Customer():
    def __init__(self, name, lastName, document, address):
        self.id = next(c)
        self.addDate = datetime.now().strftime('%d/%m/%Y:%H:%M')
        self.name = name
        self.lastName = lastName
        self.document = document
        self.address = address

if __name__ == "__main__":
    c = Customer('Rian', 'Muniz', '09984751570','a')
    print(c.id)
    c1 = Customer('Rian', 'Muniz', '09984751570','a')
    print(c1.address)

