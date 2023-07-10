#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Module to create class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)
"""


class Rectangle(BaseGeometry):
    """Class Rectangle

    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
