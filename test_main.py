import pytest
from category import Category
from product import Product

@pytest.fixture
def sample_product():
    return Product("Sample Product", "Description", 10, 50)

@pytest.fixture
def sample_category():
    return Category("Sample Category", "Category Description")

def test_add_product_to_category(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 39

def test_category_products(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert sample_category.products == "Sample Product, 10 руб. Остаток: 50 шт."

def test_count_categories(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert sample_category.count_categories() == 1

def test_product_price_setter():
    product = Product("Product", "Description", 10, 50)
    product.price = -5
    assert product.price == 10  # Цена не должна измениться из-за некорректного значения
