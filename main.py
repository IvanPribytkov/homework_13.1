class Product:
    total_products = 0  # Общее количество уникальных продуктов

    def __init__(self, name, description, price, quantity):
        """
        Инициализация объекта Product.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_products += 1  # Увеличиваем общее количество уникальных продуктов при создании нового продукта

class Category:
    total_categories = 0  # Общее количество категорий
    total_unique_products = 0  # Общее количество уникальных продуктов (не учитывая количество в наличии)

    def __init__(self, name, description):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        """
        self.name = name
        self.description = description
        self.products = []  # Список товаров в данной категории
        Category.total_categories += 1  # Увеличиваем общее количество категорий при создании новой категории

    def add_product(self, product):
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        self.products.append(product)
        Category.total_unique_products += 1  # Увеличиваем общее количество уникальных продуктов при добавлении нового продукта в категорию

