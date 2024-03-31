import pytest
from Product import Product
from Category import Category


@pytest.fixture
def sample_product():
    return Product("Sample Product", "Description", 10, 50)


@pytest.fixture
def sample_category():
    return Category("Sample Category", "Category Description")


def test_product_string_representation(sample_product):
    assert str(sample_product) == "Sample Product, 10 руб. Остаток: 50 шт."


def test_product_price_setter():
    product = Product("Product", "Description", 10, 50)
    product.price = -5
    assert product.price == 10  # Цена не должна измениться из-за некорректного значения


def test_product_addition(sample_product):
    product1 = Product("Product 1", "Description", 10, 50)
    product2 = Product("Product 2", "Description", 20, 30)
    combined_product = product1 + product2
    assert combined_product.name == "Combined Product"
    assert combined_product.price == pytest.approx(13.75, rel=1e-2)
    assert combined_product.quantity == 80


def test_add_product_to_category(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 39


def test_category_string_representation(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert str(sample_category) == "Sample Category, количество продуктов: 50 шт."


def test_count_categories(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert sample_category.count_categories() == 1
