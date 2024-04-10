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
        self.__products = []

    def add_product(self, product):
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product.")

        # Проверяем, что список __products не пустой и тип первого элемента совпадает с типом нового продукта
        if self.__products and not isinstance(product, type(self.__products[0])):
            raise TypeError("Можно добавлять только товары одной категории.")

        self.__products.append(product)

    @property
    def products(self):
        """
        Геттер для атрибута products, возвращающий список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт.
        """
        return '\n'.join(map(str, self.__products))

    def count_categories(self):
        """
        Метод для подсчета количества категорий.
        """
        return len(self.__products)

    def __str__(self):
        """Строковое представление объекта Category."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
