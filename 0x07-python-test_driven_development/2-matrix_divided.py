#!/usr/bin/python3

"""Module to divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function to divides all elements of a mattix
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0 or div == float('inf'):
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    row_size = len(matrix[0])
    for r in matrix:
        if type(r) != list or len(r) == 0:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        if len(r) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        col = []
        for c in r:
            if type(c) not in [int, float]:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

            col.append(round(c / div, 2))
        new_matrix.append(col)
    return (new_matrix)
