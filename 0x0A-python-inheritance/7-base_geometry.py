#!/usr/bin/python3

"""Module Write a class BaseGeometry
    (based on 6-base_geometry.py)

"""


class BaseGeometry:
    """BaseGeometry class

    """
    def area(self):
        """Raise and Exception

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value argument

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
