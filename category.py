from logmixin import LogMixin
from product import Product

class Category(LogMixin):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product.")

        if product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")

        if self.__products and not isinstance(product, type(self.__products[0])):
            raise TypeError("Можно добавлять только товары одной категории.")

        self.__products.append(product)

    @property
    def products(self):
        return '\n'.join(map(str, self.__products))

    def count_categories(self):
        return len(self.__products)

    def average_price(self):
        total_price = sum(product.price for product in self.__products)
        total_count = len(self.__products)

        try:
            average_price = total_price / total_count
        except ZeroDivisionError:
            print("В категории нет товаров.")
            return 0

        return average_price

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
