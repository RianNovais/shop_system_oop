from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pathlib import Path
from datetime import datetime


class Excel():
    def __init__(self):
        self.pathproductspreadsheet = Path().absolute() / 'spreadsheets' / 'products.xlsx'
        self.pathcustomerspreadsheet = Path().absolute() / 'spreadsheets' / 'customers.xlsx'
        self.pathsalespreadsheet = Path().absolute() / 'spreadsheets' / 'sales.xlsx'
        self.updateDate = datetime.now().strftime('%d/%m/%Y:%H/%M')

    def export_products_to_xlsx(self, listProducts):
        #creating workbook and create an sheet and remove "Sheet" default

        workbook = Workbook()
        workbook.create_sheet('Products')
        del workbook['Sheet']
        #workbook.active is sheet "Products"
        worksheet: Worksheet = workbook.active

        #add headers
        worksheet.cell(1, 1, 'Id')
        worksheet.cell(1, 2, 'Add Date')
        worksheet.cell(1, 3, 'Name')
        worksheet.cell(1, 4, 'Manufacturer')
        worksheet.cell(1, 5, 'Serial Number')
        worksheet.cell(1, 6, 'Category')
        worksheet.cell(1, 7, 'Quantity')
        worksheet.cell(1, 8, 'Price')


        #pra cada produto ele gera uma lista com os valores dos atributos e adiciona cada item respectivamente
        #em cada linha com o .append (ele já reconhece que nossa 1 linha possui nossos titulos)
        for product in listProducts:
            prod = [product.id, product.addDate, product.name, product.manufacturer, product.serialNumber,
                    product.category.value, product.quantity, product.price]
            worksheet.append(prod)

        #save and showing success message
        workbook.save(self.pathproductspreadsheet)
        print(f'{worksheet.max_row -1} lines of products add sucessfully to products.xlsx')

    def export_customers_to_xlsx(self, listCustomers):
        workbook = Workbook()
        workbook.create_sheet('Customers')
        del workbook['Sheet']
        worksheet: Worksheet = workbook.active

        #definindo headers de forma simplificada, passando uma lista com os titulos que queremos
        #pro worksheet.append, nesse caso ele vai preencher a nossa primeira linha com cada titulo em cada
        #coluna, formando nosso cabeçalho
        headers = ['Id', 'Add Date', 'Name', 'LastName', 'Document', 'Address']
        worksheet.append(headers)



        for customer in listCustomers:
            cust = [customer.id, customer.addDate, customer.name, customer.lastName, customer.document, customer.address]
            worksheet.append(cust)

        workbook.save(self.pathcustomerspreadsheet)
        print(f'{worksheet.max_column -1} lines of customers add sucessfully to customers.xlsx')

    def export_sales_to_xlsx(self, listSales):
        workbook = Workbook()
        workbook.create_sheet('Sales')
        del workbook['Sheet']

        worksheet: Worksheet = workbook.active


        #add headers
        headers = ['Sale Date', 'Customer', 'Product', 'Quantity']
        worksheet.append(headers)

        for sale in listSales:
            sal = [sale.saleDate, sale.customer.name, sale.product.name, sale.quantity]
            worksheet.append(sal)


        workbook.save(self.pathsalespreadsheet)
        print(f'{worksheet.max_row -1} lines of sales add sucessfully to products.xlsx')



if __name__ == "__main__":
    e = Excel()
    e.export_products_to_xlsx()
