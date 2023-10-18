
from product import Product
from customer import Customer
from sale import Sale

class Shop():
    def __init__(self):
        self.products:list[Product] =[]
        self.customers:list[Customer] = []
        self.sales:list[Sale] = []


    def add_product(self, name, manufacturer, serialNumber, category, quantity, price):
        p = Product(name, manufacturer, serialNumber, category, quantity, price)
        self.products.append(p)
        print(f'product {name} add sucessfully')

    def add_customer(self, name, lastName, document, address):
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

        #Funções que verificam se com os ids passados existem o cliente, o produto, e depois verifica a quantidade
        #do produto, se a quantidade que o cliente quer levar não é maior que a existente do produto
        #caso o id do produto do cliente, ou a quantidade for insuficiente, é lançado um ValueError
        #caso exista o cliente ou o produto, é retornado o cliente e o produto ao invés de um erro
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
            if quantity > product.quantity:
                raise ValueError('Insufficient quantity of product')
            else:
                product.quantity = product.quantity - quantity
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
        #é instanciada uma venda passando o cliente o produto e a quantidade
        s = Sale(customer, product, quantity)
        self.sales.append(s)
        print('SALE MADE SUCCESSFULLY')

    def export_data_xlsx(self):
        ...


if __name__ == "__main__":
    ...