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

            Args:
                name (str): The first argument
                value (int): The value to vlidate

            Raises:
                TypeError: if value is not an integer
                ValueError: if value is less or equal to 0

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
