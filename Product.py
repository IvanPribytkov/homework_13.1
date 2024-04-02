from abc import ABC, abstractmethod

class Product(ABC):
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
        self._price = price
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

    @abstractmethod
    def __repr__(self):
        pass
