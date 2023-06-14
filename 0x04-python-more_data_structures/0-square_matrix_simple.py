#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda r: list(map(lambda c: c * c, r)), matrix))
    return (new_matrix)
