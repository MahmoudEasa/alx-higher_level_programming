#!/usr/bin/python3

"""Module to create function that adds a new attribute
    to an object if it’s possible

"""


def add_attribute(mc, name, value):
    """Function to adds a new attribute

        Args:
            mc (object): The object
            name (str): The name
            value (str): The value
    """

    if hasattr(mc, '__dict__'):
        setattr(mc, name, value)
    else:
        raise TypeError("can't add new attribute")
