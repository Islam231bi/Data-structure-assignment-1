import numpy as np

"""Generating random array with the given size using numpy library."""
"""Make sure to install numpy before running the code."""


class Generate:
    def __init__(self):
        self.array = []

    def generate(self, size):
        # randint takes 3 parameters (first, last, size)
        # first and last parameter specify the range of generated random numbers
        self.array = np.random.randint(1, 100000, size)
        return self.array
