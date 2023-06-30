#!/usr/bin/python3
"""Class MagicClass that does Python bytecode"""
import math


class MagicClass:
    """Class does Python bytecode"""

    def __init__(self, radius=0):
        """Initial Data
        
            Args:
                radius (int or float): the radius magic class
        """

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Return circumference"""
        return (2 * math.pi * self.__radius)
