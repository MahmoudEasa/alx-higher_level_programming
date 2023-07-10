#!/usr/bin/python3

"""Module to create class Square that inherits from Rectangle
    (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Rectangle

        Attribute:
            size (int): The size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
