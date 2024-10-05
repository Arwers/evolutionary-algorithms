import numpy as np
import pytest
from Core.chromosome import Chromosome, INVALID_SIZE, INVALID_VALUES

BOUNDARIES = (-5, 5)
PRECISION = 2

@pytest.fixture
def chromosome():
    np.random.seed(1)
    return Chromosome(BOUNDARIES, PRECISION)

def test_decode_chromosome(chromosome):
    assert chromosome.decode_chromosome() == 3.113391984359726

def test_size(chromosome):
    assert chromosome.size() == 10

def test_invalid_size(chromosome):
    with pytest.raises(Exception) as excinfo:
        chromosome.set_chromosome(np.array([0, 1, 0, 1, 0, 1, 0]))
    assert str(excinfo.value) == INVALID_SIZE

def test_invalid_values(chromosome):
    with pytest.raises(Exception) as excinfo:
        chromosome.set_chromosome(np.array([5, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert str(excinfo.value) == INVALID_VALUES