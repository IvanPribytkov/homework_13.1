import pytest
from smartphone import Smartphone

@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone", "Description", 1000, 10, "High", "X", 128, "Black")

def test_smartphone_initialization(sample_smartphone):
    assert sample_smartphone.name == "iPhone"
    assert sample_smartphone.description == "Description"
    assert sample_smartphone.price == 1000
    assert sample_smartphone.quantity == 10
    assert sample_smartphone.performance == "High"
    assert sample_smartphone.model == "X"
    assert sample_smartphone.storage_capacity == 128
    assert sample_smartphone.color == "Black"
