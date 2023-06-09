#!/usr/bin/python3

"""Module to adds 2 integer



"""


def add_integer(a, b=98):
    """Function to adds 2 integers
        Return: (int)a + (int)b
    """

    if type(a) not in [int, float] or\
        a == float('inf') or a == -float('inf')\
            or a != a:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or\
        b == float('inf') or b == -float('inf')\
            or b != b:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
