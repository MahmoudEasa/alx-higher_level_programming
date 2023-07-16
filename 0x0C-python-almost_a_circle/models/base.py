#!/usr/bin/python3

"""The first Module

"""
import json


class Base:
    """The first Class

        Attributes:
            __nb_objects (int): to manage id attribute in all future classes
            id (int): The id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

            Args:
                list_dictionaries (list): list of dictionaries

            Return:
                If list_dictionaries is None or empty,
                    return the string: "[]"
                Otherwise, return the JSON string
                    representation of list_dictionaries
        """

        if list_dictionaries is None:
            return ("[]")

        if isinstance(list_dictionaries, list):
            list_len = len(list_dictionaries)

            if list_len == 0:
                return ("[]")

            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
            of list_objs to a file

            Args:
                list_objs (list): list of instances who inherits of Base
        """

        file_name = cls.__name__ + ".json"
        json_arr = []
        if isinstance(list_objs, list) and len(list_objs) > 0:
            for obj in list_objs:
                json_arr.append(obj.to_dictionary())

        json_str = Base.to_json_string(json_arr)

        with open(file_name, "w") as f:
            f.write(json_str)
