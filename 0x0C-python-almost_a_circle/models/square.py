#!/usr/bin/python3

"""Module to create class Square that inherits from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument args to each attribute
           or assigns a key/value argument kwargs to attributes

           Args:
               args (list): list of values
               kwargs (dict): dictionary of keys and values
        """

        args_len = len(args)
        kwargs_len = len(kwargs)
        dics = list(self.__dict__.keys())

        if (args_len):
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except (IndexError):
                pass

        elif (kwargs_len):
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'size':
                    self.width = val
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        """
        res = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
            }
        return (res)
