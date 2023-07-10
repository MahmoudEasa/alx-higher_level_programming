#!/usr/bin/python3

"""Module to create class MyInt that inherits from int

"""


class MyInt(int):
    """Class MyInt

    """

    def __eq__(self, other):
        return (str(self) != str(other))

    def __ne__(self, other):
        return (str(self) == str(other))
