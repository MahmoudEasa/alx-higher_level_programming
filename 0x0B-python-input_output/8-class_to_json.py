#!/usr/bin/python3
"""Module to write a function that returns
    the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

"""


def class_to_json(obj):
    """Function Class to json

        Args:
            obj (object): an instance of a Class
    """

    return (obj.__dict__)
