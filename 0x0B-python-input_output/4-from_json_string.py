#!/usr/bin/python3
"""Module to create function that returns an object
    (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Function to create function that returns an object
        (Python data structure) represented by a JSON string

        Args:
            my_str (str): The string
    """

    return (json.loads(my_str))
