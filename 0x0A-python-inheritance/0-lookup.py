#!/usr/bin/python3

"""Module to returns the list of available attributes
    and methods of an object

"""


def lookup(obj):
    """Function to returns the list of available attributes
        and methods of an object

        Args:
            obj (obj): object

        Return:
            list obj
    """
    if isinstance(obj, object):
        return (list(obj.__dict__))

