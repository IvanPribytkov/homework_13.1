from product import Product  # Импортируем класс Product

class Category:
    total_categories = 0  # Общее количество категорий
    total_unique_products = 0  # Общее количество уникальных продуктов (не учитывая количество в наличии)

    def __init__(self, name: str, description: str):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        """
        self.name = name
        self.description = description
        self._products = []  # Приватный атрибут - список товаров в данной категории
        # Увеличиваем общее количество категорий при создании новой категории
        Category.total_categories += 1

    def add_product(self, product: Product):
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        self._products.append(product)
        Category.total_unique_products += 1  # Увеличиваем общее количество уникальных продуктов при добавлении нового продукта в категорию
