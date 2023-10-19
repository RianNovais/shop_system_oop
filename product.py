from itertools import count
from datetime import datetime
from productCategory import ProductCategory

c = count(start=1)

def choice_category(categoryName: str)->str or None:
    if categoryName == ProductCategory.DEFAULT:
        return productCategory.DEFAULT
    if categoryName.lower() == "eletronics":
        return ProductCategory.ELECTRONICS
    elif categoryName.lower() == "clothing":
        return ProductCategory.CLOTHING
    elif categoryName.lower() == "food":
        return ProductCategory.FOOD
    elif categoryName.lower() == "books":
        return ProductCategory.BOOKS
    elif categoryName is None:
        print('Invalid category')
        return ProductCategory.DEFAULT
    else:
        print('Invalid category')
        return ProductCategory.DEFAULT

class Product():
    def __init__(self, name: str, manufacturer: str, serialNumber: str, quantity: int, price: float, category: ProductCategory=ProductCategory.DEFAULT):
        self.id = next(c)
        self.addDate = datetime.now().strftime('%d/%m/%Y:%H:%M')
        self.name = name
        self.manufacturer = manufacturer
        self.serialNumber = serialNumber
        self.category = choice_category(category)
        self.quantity = quantity
        self.price = price



if __name__ == "__main__":
    p = Product('TV 50 POLEGADAS', 'Samsung', '1366', 10, 100, 'Eletronics')
    print(p.category.value)

