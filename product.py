from abstractproduct import AbstractProduct
from logmixin import LogMixin

class Product(AbstractProduct, LogMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены."""
        if value <= 0:
            raise ValueError("Ошибка: Цена должна быть больше нуля.")
        else:
            self._price = value

    def __repr__(self):
        """Строковое представление объекта Product."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
