#!/usr/bin/python3

"""The first Module

"""


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
