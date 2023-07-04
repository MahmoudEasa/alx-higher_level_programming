#!/usr/bin/python3

"""Module to LockedClass
"""


class LockedClass:
    """Class LockedClass"""

    __slots__ = ['first_name']

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(f"'LockedClass'\
 object has no attribute '{key}'")
        super().__setattr__(key, value)
