import pytest
from individual import Individual

class TestIndividual:
    def setup_method(self):
        self.individual = Individual(genes=5, precision=6, bundaries=(-5, 5))

    def test_setter():
        have = Individual.get_size()
        want = 5
        assert have == want