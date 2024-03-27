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

    def __str__(self):
        """Строковое представление объекта Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение объектов Product."""
        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        total_quantity = self.quantity + other.quantity
        return Product("Combined Product", "Combined Description", total_price / total_quantity, total_quantity)
