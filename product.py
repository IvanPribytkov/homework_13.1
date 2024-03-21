class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта Product.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены."""
        if value <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
        else:
            self._price = value


product = Product("Phone", "Smartphone", 500, 10)
print(product.price)  # Выведет: 500

# Установка новой корректной цены
product.price = 600
print(product.price)  # Выведет: 600

# Попытка установить некорректную цену
product.price = -100  # Выведет сообщение об ошибке
print(product.price)  # Выведет: 600 (цена останется прежней)
