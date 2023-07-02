#!/usr/bin/python3

"""Module to print a square with the character #
"""


def print_square(size):
    """Function to print a square with the character #

        Args:
            size (int): the size length of the square
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
