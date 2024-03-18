import pytest
from main import Category, Product

@pytest.fixture(autouse=True)
def setup():
    Product.total_products = 0
    Category.total_categories = 0
    Category.total_unique_products = 0

def test_category_initialization():
    category = Category("Test Category", "Test Description")
    assert category.name == "Test Category"
    assert category.description == "Test Description"

def test_product_initialization():
    product = Product("Test Product", "Test Description", 10.99, 100)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 10.99
    assert product.quantity == 100

def test_count_products():
    product1 = Product("Product 1", "Description 1", 9.99, 50)
    product2 = Product("Product 2", "Description 2", 19.99, 30)
    assert Product.total_products == 2

def test_count_categories():
    category1 = Category("Category 1", "Description 1")
    category2 = Category("Category 2", "Description 2")
    assert Category.total_categories == 2
