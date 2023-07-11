#!/usr/bin/python3
"""Module to create function that writes
    an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """Function to create function that writes
        an Object to a text file, using a JSON representation:

        Args:
            my_obj (object): The object
            filename (str): The file name
    """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
