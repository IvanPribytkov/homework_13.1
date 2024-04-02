import pytest
from Grass import Grass

@pytest.fixture
def sample_grass():
    return Grass("Lawn Grass", "Description", 5, 100, "USA", "2 weeks", "Green")

def test_grass_initialization(sample_grass):
    assert sample_grass.name == "Lawn Grass"
    assert sample_grass.description == "Description"
    assert sample_grass.price == 5
    assert sample_grass.quantity == 100
    assert sample_grass.country_of_origin == "USA"
    assert sample_grass.germination_period == "2 weeks"
    assert sample_grass.color == "Green"
