import pytest
from category import Category
from product import Product

@pytest.fixture
def sample_data():
    category1 = Category("Electronics", "Electronics category")
    category2 = Category("Clothing", "Clothing category")

    product1 = Product("Laptop", "Gaming laptop", 1500, 10)
    product2 = Product("T-shirt", "Cotton T-shirt", 20, 50)

    # Добавляем продукты в категории
    category1.add_product(product1)
    category2.add_product(product2)

    return category1, category2, product1, product2

# Тесты для класса Category
def test_category_initialization(sample_data):
    category1, category2, _, _ = sample_data

    assert category1.name == "Electronics"
    assert category1.description == "Electronics category"
    assert category2.name == "Clothing"
    assert category2.description == "Clothing category"

def test_category_product_count(sample_data):
    category1, category2, product1, product2 = sample_data

    assert len(category1.products) == 1
    assert len(category2.products) == 1

def test_total_categories_count(sample_data):
    assert Category.total_categories == 2

def test_total_unique_products_count(sample_data):
    assert Product.total_products == 2

# Тесты для класса Product
def test_product_initialization(sample_data):
    _, _, product1, product2 = sample_data

    assert product1.name == "Laptop"
    assert product1.description == "Gaming laptop"
    assert product1.price == 1500
    assert product1.quantity == 10

    assert product2.name == "T-shirt"
    assert product2.description == "Cotton T-shirt"
    assert product2.price == 20
    assert product2.quantity == 50

def test_total_products_count(sample_data):
    assert Product.total_products == 2

