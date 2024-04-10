import pytest
from unittest.mock import MagicMock

from category import Category
from product import Product

@pytest.fixture
def sample_product():
    mock_product = MagicMock(spec=Product)
    mock_product.name = "Sample Product"
    mock_product.description = "Description"
    mock_product.price = 10
    mock_product.quantity = 50
    return mock_product

def test_add_product_to_category(sample_product):
    category = Category("Sample Category", "Category Description")
    category.add_product(sample_product)
    assert len(category.products.split('\n')) == 1  # Разделить строку и подсчитать количество элементов

def test_count_categories(sample_product):
    category = Category("Sample Category", "Category Description")
    category.add_product(sample_product)
    assert category.count_categories() == 1
