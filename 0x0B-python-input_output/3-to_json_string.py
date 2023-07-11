#!/usr/bin/python3
"""Module to create function that returns
    the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Function to create function that returns
        the JSON representation of an object (string)

        Args:
            my_obj (object): The object
    """

    return (json.dumps(my_obj))
