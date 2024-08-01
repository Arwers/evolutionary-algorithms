import pytest
import numpy as np
from individual import Individual

class TestIndividual:
    def setup_method(self):
        self.individual = Individual(genes=5, boundaries=(-5, 5), precision=6)

    def test_size(self):
        have = self.individual.get_size()
        want = 5
        assert have == want
