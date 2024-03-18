import pytest
from category import Category
from product import Product

@pytest.fixture
def product_fixture():
    product1 = Product("Product 1", "Description 1", 9.99, 50)
    product2 = Product("Product 2", "Description 2", 19.99, 30)
    return [product1, product2]

def test_category_initialization():
    category = Category("Category 1", "Description 1", [])
    assert category.name == "Category 1"
    assert category.description == "Description 1"
    assert category.products == []

def test_count_products(product_fixture):
    assert Product.total_products == 2

def test_count_categories():
    category1 = Category("Category 1", "Description 1", [])
    category2 = Category("Category 2", "Description 2", [])
    assert Category.total_categories == 3
