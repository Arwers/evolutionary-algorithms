import numpy as np
import math

# Error handling messanges
INVALID_SIZE = "Invalid size of the new chromosome."
INVALID_VALUES = "Invalid number range in new chromosome."


class Chromosome:
    """
    Represents single argument in a function.

            Parameters:
                    boundaries (tuple): a boundary for generating a variable, in (a, b) format
                    precision (int): Number of significant figures
    """

    def __init__(self, boundaries, precision):
        self.a, self.b = boundaries
        self.precision = precision

        # generate chromosome
        self.m = math.ceil(math.log2((self.b - self.a) * 10**self.precision))
        self.chromosome = np.random.randint(2, size=self.m)

    """
    Returns the decimal representation of the chromosome.

            Returns:
                    decimal representation (float): decimal representation of a chromosome 
    """

    def decode_chromosome(self):
        binary_string = "".join(map(str, self.chromosome))
        decimal_value = int(binary_string, 2)
        return self.a + decimal_value * (self.b - self.a) / (2**self.m - 1)

    """
    Returns the chromosome as a binary numpy.array.

            Returns:
                    chromosome (numpy.array): Binary array of chromosome representation
    """

    def get_chromosome(self):
        return self.chromosome

    """
    Set a chromosome content to provided array.
            Parameters:
                    new_chromosome (numpy.array): new chromosome with exact size and values in [1, 0] 
            Raises:
                    INVALID_VALUES (Exception): at least one value of new chromosome not in [0, 1]
                    INVALID_SIZES (Exception): provided chromosome have different size than original
    """

    def set_chromosome(self, new_chromosome):
        if np.size(new_chromosome) == np.size(self.chromosome):
            for num in new_chromosome:
                if num not in (0, 1):
                    raise Exception(INVALID_VALUES)
            self.chromosome = new_chromosome
        else:
            raise Exception(INVALID_SIZE)
