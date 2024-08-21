from typing import List
import numpy as np
import math

# Error handling messanges
INVALID_SIZE = "Invalid size of the new chromosome."
INVALID_VALUES = "Invalid number range in new chromosome."


class Chromosome:
    """## Chromosome class represents a chromosome in the population.\n
    The chromosome is represented as a binary string.\n

    ### Parameters
    - **boundaries**: tuple of two numbers representing the boundaries of the chromosome values. eg. (-5, 5)
    - **precision**: integer representing the decimal precision of the chromosome values. eg. 6

    ### Attributes
    - **a**: lower boundary of the chromosome values
    - **b**: upper boundary of the chromosome values
    - **precision**: decimal precision of the chromosome values
    - **m**: number of bits in the binary chromosome
    - **chromosome**: numpy.ndarray of binary values

    ### Methods
    - **decode_chromosome()**: Decode the binary chromosome to a decimal value.
    - **get_chromosome()**: Get the binary chromosome.
    - **set_chromosome(new_chromosome)**: Set a new binary chromosome.
    - **size()**: Get the size of the chromosome.
    """

    def __init__(
        self, 
        boundaries: tuple,
        precision: int,
    ):
        self.a, self.b = boundaries
        self.precision = precision

        # generate chromosome
        self.m = math.ceil(math.log2((self.b - self.a) * 10**self.precision))
        self.chromosome = np.random.randint(2, size=self.m)

    def __str__(self):
        return np.array2string(self.chromosome, separator=", ", precision=2)

    def decode_chromosome(self) -> float:
        """## Decode the binary chromosome to a decimal value.\n
        ### Returns
        - **float**: list of decimal values
        ### Example
        chromosome = Chromosome((-5, 5), 6)\n
        chromosome.decode_chromosome() \n
        Output: [-2.5]
        """
        binary_string = "".join(map(str, self.chromosome))
        decimal_value = int(binary_string, 2)
        return self.a + decimal_value * (self.b - self.a) / (2**self.m - 1)

    def get_chromosome(self) -> List[np.array]:
        """## Get the binary chromosome.\n

        ### Returns
        - **numpy.ndarray**: binary chromosome
        """
        return self.chromosome

    def set_chromosome(self, new_chromosome):
        """## Set a new binary chromosome.\n
        ### Parameters
        - **new_chromosome**: numpy.ndarray of binary values

        ### Raises
        - **Exception**: INVALID_SIZE if the new chromosome size is different from the current chromosome size.
        - **Exception**: INVALID_VALUES if the new chromosome values are not 0 or 1.

        ### Example
        chromosome = Chromosome((-5, 5), 6)\n
        chromosome.set_chromosome(np.array([0, 1, 0, 1, 0, 1]))\n
        """
        if np.size(new_chromosome) == np.size(self.chromosome):
            for num in new_chromosome:
                if num not in (0, 1):
                    raise Exception(INVALID_VALUES)
            self.chromosome = new_chromosome
        else:
            raise Exception(INVALID_SIZE)

    def size(self) -> int:
        return np.size(self.chromosome)
