from itertools import count
from datetime import datetime


# customer class, which receives several attributes, including the current instantiation date and an
# automatically incremented ID


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
    ...

