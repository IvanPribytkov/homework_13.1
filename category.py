from product import Product

class Category:
    def __init__(self, name: str, description: str):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        """
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут - список товаров в данной категории

    def add_product(self, product: Product):
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        self.__products.append(product)

    @property
    def products(self):
        """
        Геттер для атрибута products, возвращающий список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт.
        """
        return '\n'.join([f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products])

    def count_categories(self):
        """
        Метод для подсчета количества категорий.
        """
        return len(self.__products)