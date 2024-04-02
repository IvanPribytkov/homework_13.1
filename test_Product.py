import pytest
from unittest.mock import MagicMock
from Product import Product

@pytest.fixture
def sample_product():
    mock_product = MagicMock(spec=Product)
    mock_product.name = "Sample Product"
    mock_product.description = "Description"
    mock_product.price = 10
    mock_product.quantity = 50
    return mock_product

def test_product_initialization(sample_product):
    assert sample_product.name == "Sample Product"
    assert sample_product.description == "Description"
    assert sample_product.price == 10
    assert sample_product.quantity == 50
