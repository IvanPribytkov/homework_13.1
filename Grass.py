from Product import Product

class Grass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country_of_origin: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return f"Grass('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.country_of_origin}', '{self.germination_period}', '{self.color}')"
