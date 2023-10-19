
from product import Product
from customer import Customer
from sale import Sale
from ssheet import Excel

# Here, in the "Shop" class, we have a kind of hub for connecting to various classes in our system, such as customers,
# sales, products, and in this class we define all the methods for creating, listing, selling and exporting to XLSX,
# and previously an Excel object is instantiated to access the class and perform the export, which is done using specific
# methods for products, customers and sales.


e = Excel()

class Shop():
    def __init__(self):
        self.products:list[Product] =[]
        self.customers:list[Customer] = []
        self.sales:list[Sale] = []

    def add_product(self):
        name = input('Name: ')
        manufacturer = input('Manufacturer: ')
        serialNumber = input('Serial Number: ')
        category = input('Category: ')
        quantity = int(input('Quantity: '))
        price = float(input('Price: R$ '))

        p = Product(name, manufacturer, serialNumber, quantity, price, category)
        self.products.append(p)
        print(f'product {name} add sucessfully')
    def add_customer(self):
        name = input('Name: ')
        lastName = input('Last Name: ')
        document = input('Document: ')
        address = input('Address: ')
        c = Customer(name, lastName, document, address)
        self.customers.append(c)
        print(f'customer {name} {lastName} add sucessfully')
    def list_products(self):
        for product in self.products:
            print(f'Id: {product.id} | AddDate: {product.addDate} | Name: {product.name} |'
                  f' Manufacturer: {product.manufacturer} | SerialNumber: {product.serialNumber} | Category:'
                  f' {product.category.value} | Quantity: {product.quantity} | Price: {product.price}')
        print('')
    def list_customers(self):
        for customer in self.customers:
            print(f'Id: {customer.id} | AddDate: {customer.addDate} | Name: {customer.name} | LastName: '
                  f'{customer.lastName} | Document: {customer.document} | Address: {customer.address}')

        print('')
    def make_sale(self):

        # Functions that check whether the customer, the product exist with the passed ids, and then check the quantity
        # of the product, if the quantity that the customer wants to take is not greater than the existing quantity of the product
        # if the customer's product id, or the quantity is insufficient, a ValueError is thrown
        # if the customer or the product exists, the customer and the product are returned instead of an error
        def verify_customer(idCustomer):
            for customer in self.customers:
                if customer.id == idCustomer:
                    return customer
            raise ValueError('Customer not found with this ID')

        def verify_product(idProduct):
            for product in self.products:
                if product.id == idProduct:
                    return product
            raise ValueError('Product not found with this ID')

        def verify_quantity_product(product, quantity):
            if quantity > int(product.quantity):
                raise ValueError('Insufficient quantity of product')
            else:
                product.quantity = int(product.quantity) - quantity
                print(f'Sale made of product: {product.name} with quantity: {quantity} currently available quantity: {product.quantity}')
                return

        idCustomer = int(input('Id of the customer who will make the purchase '))
        if verify_customer(idCustomer) is not None:
            customer = verify_customer(idCustomer)

        idProduct = int(input('Id of the product you want to buy: '))
        if verify_product(idProduct) is not None:
            product = verify_product(idProduct)

        print(f'What quantity of product : {product.name} want to buy. {product.quantity} available')
        quantity = int(input(''))

        verify_quantity_product(product, quantity)
        # a sale is instantiated by passing the customer the product and the quantity
        s = Sale(customer, product, quantity)
        self.sales.append(s)
        print('SALE MADE SUCCESSFULLY')
    def export_products_xlsx(self):
        e.export_products_to_xlsx(self.products)
    def export_customers_xlsx(self):
        e.export_customers_to_xlsx(self.customers)
    def export_sales_xlsx(self):
        e.export_sales_to_xlsx(self.sales)

if __name__ == "__main__":
    ...



