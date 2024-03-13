import unittest
from main import Product, Category

class TestProductCategory(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Laptop", "Powerful laptop", 999.99, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "Powerful laptop")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.quantity, 10)

    def test_category_creation(self):
        category = Category("Electronics", "Electronic devices")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic devices")
        self.assertEqual(category.products, [])

    def test_add_product_to_category(self):
        category = Category("Electronics", "Electronic devices")
        product = Product("Laptop", "Powerful laptop", 999.99, 10)
        category.products.append(product)
        self.assertEqual(len(category.products), 1)
        self.assertEqual(category.products[0].name, "Laptop")

if __name__ == '__main__':
    unittest.main()
