#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Module to create class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)


"""


class Rectangle(BaseGeometry):
    """Class Rectangle

        Attributes:
            width (int): The width
            height (int): The height

    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
