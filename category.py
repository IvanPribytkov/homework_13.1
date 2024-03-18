from product import Product  # Импортируем класс Product

class Category:
    total_categories = 0  # Общее количество категорий
    total_unique_products = 0  # Общее количество уникальных продуктов (не учитывая количество в наличии)

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в данной категории.
        """
        self.name = name
        self.description = description
        self.products = products
        # Увеличиваем общее количество категорий при создании новой категории
        Category.total_categories += 1
        # Увеличиваем общее количество уникальных продуктов при создании новой категории
        Product.total_products += len(products)

    def add_product(self, product: Product):
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        self.products.append(product)
        Category.total_unique_products += 1  # Увеличиваем общее количество уникальных продуктов при добавлении нового продукта в категорию
