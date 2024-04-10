from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    """
    Абстрактный класс продукта.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для цены."""
        pass

    def __repr__(self):
        """Магический метод для вывода информации о создаваемом объекте."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
