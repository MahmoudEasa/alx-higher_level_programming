#!/usr/bin/python3
"""Module to create function that
    creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Function to create function that
        creates an Object from a “JSON file”

        Args:
            filename (str): The file name
    """

    with open(filename, "r") as f:
        json_load = f.read()
        return (json.loads(json_load))
