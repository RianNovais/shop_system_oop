from shop import Shop

#main module

s = Shop()

#menu for user interaction, calls the add, remove, sell and export functions to XSLX found in "shop" class

while True:
    choiceUser = int(input('1-Add- Customer\n2-Add Product\n3-List Products\n4-List Customers\n5-Make Sale\n6-Export Products to XLSX'
                           '\n7-Export Customers to XLSX\n8-Export Sales to XLSX\n9-Exit\n'))

    if choiceUser == 1:
        s.add_customer()
    elif choiceUser == 2:
        s.add_product()
    elif choiceUser == 3:
        s.list_products()
    elif choiceUser == 4:
        s.list_customers()
    elif choiceUser == 5:
        s.make_sale()
    elif choiceUser == 6:
        s.export_products_xlsx()
    elif choiceUser == 7:
        s.export_customers_xlsx()
    elif choiceUser == 8:
        s.export_sales_xlsx()
    elif choiceUser == 9:
        print('EXITING...')
        break
    else:
        print('enter a valid choice')


