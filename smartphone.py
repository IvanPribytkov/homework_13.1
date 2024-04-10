from product import Product

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, performance: str, model: str, storage_capacity: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def __repr__(self):
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.performance}', '{self.model}', {self.storage_capacity}, '{self.color}')"
