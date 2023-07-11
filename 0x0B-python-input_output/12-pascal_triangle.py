#!/usr/bin/python3
"""Module to Create a function that returns a list of lists
    of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Function pascal_triangle

        Args:
            n (int): integer
    """
    if n <= 0:
        return ([])

    result = [[1]]
    for i in range(n - 1):
        prev = 0
        arr = []
        for j in range(len(result[i])):
            arr.append(result[i][j] + prev)
            prev = result[i][j]
        arr.append(1)
        result.append(arr)

    return (result)
