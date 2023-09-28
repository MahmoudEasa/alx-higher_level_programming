#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers
    """

    if type(list_of_integers) is not list:
        return (None)

    list_len = len(list_of_integers)
    if list_len == 0:
        return (None)

    if list_len < 3:
        return (max(list_of_integers))

    list_of_integers.sort()
    return (list_of_integers[-1])
