#!/usr/bin/python3

"""Module for prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Function for prints My name is <first name> <last name>
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
