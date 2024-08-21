import pytest
import numpy as np
from core.chromosome.chromosome import Chromosome, INVALID_SIZE, INVALID_VALUES


class TestChromosome:
    def setup_method(self):
        self.chromosome = Chromosome(boundaries=(-5, 5), precision=6)

    def test_setter(self):
        self.chromosome.set_chromosome(
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
        )
        have = self.chromosome.get_chromosome()
        want = [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
        assert have == want

    def test_invalid_setter_size(self):
        with pytest.raises(Exception, match=INVALID_SIZE):
            self.chromosome.set_chromosome([0, 1, 0])

    def test_invalid_setter_values(self):
        with pytest.raises(Exception, match=INVALID_VALUES):
            self.chromosome.set_chromosome(
                [7, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
            )
