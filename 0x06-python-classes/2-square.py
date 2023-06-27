#!/usr/bin/python3

"""Class Square that defines a square"""


class Square:
    """class Square

    """
    def __init__(self, size=0):
        """The Initial Attributes

            Attributes:
                size (int): Private instance attribute
        """

        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            print("size must be an integer")
