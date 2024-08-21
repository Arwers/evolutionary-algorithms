import numpy as np
from Core.chromosome import Chromosome
from typing import List
import copy as cp


class Individual:
    """## Individual class is a representation of a single individual in the population.\n
    The individual is represented as a list of Chromosome instances.\n

    ### Parameters
    - **boundaries**: tuple with the lower and upper boundaries for the chromosome values
    - **precision**: integer representing the decimal precision of the chromosome values
    - **no_variables**: number of variables in the individual (f(x, y, z) -> 3 variables)

    ### Attributes
    - **genes**: number of genes in the individual
    - **individual**: list of Chromosome instances

    ### Methods
    - **get_binary_variables()**: Get the binary representation of the individual.
    - **get_decimal_variables()**: Get the decimal representation of the individual.
    """

    def __init__(
        self,
        boundaries: tuple,
        precision: int,
        no_variables: int,
    ):
        self.genes = no_variables
        self.individual = np.array(
            [Chromosome(boundaries, precision) for _ in range(no_variables)]
        )

    def get_binary_variables(self) -> List[np.array]:
        """## Get the binary representation of the individual.\n
        ### Returns
        - **numpy.ndarray**: binary representation of the individual (multiple chromosomes)
        """
        return self.individual

    def get_decimal_variables(self) -> List[np.array]:
        """## Get the decimal representation of the individual.\n
        ### Returns
        - **numpy.ndarray**: decimal representation of the individual (multiple chromosomes)
        """
        variables = np.array([chr.decode_chromosome() for chr in self.individual])
        return variables

    def __deepcopy__(self, memo):
        # Create a deep copy of the Individual, including deep copies of each Chromosome
        new_copy = Individual.__new__(Individual)
        new_copy.genes = self.genes
        new_copy.individual = np.array(
            [cp.deepcopy(chr, memo) for chr in self.individual]
        )
        return new_copy
