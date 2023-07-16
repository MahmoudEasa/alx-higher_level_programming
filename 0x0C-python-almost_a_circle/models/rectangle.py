#!/usr/bin/python3

"""Module to create class Rectangle that inherits from Base

"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle

        Attributes:
            __width (int): The width
            __height (int): The height
            __x (int): The x
            __y (int): The y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id:
            self.id = id

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ Return area value of th Rectangle """
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the rectangle instance with the character #
        """

        if (self.__height and self.__width):
            for h in range(self.__y):
                print()

            for i in range(self.__height):
                print(" " * self.__x, end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}")

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
            self.__dict__['id'] = args[0]

            for i in range(1, args_len):
                if isinstance(args[i], int):
                    self.__dict__[dics[i]] = args[i]

        elif (kwargs_len):
            for key, val in kwargs.items():
                if key != 'id':
                    attr = f"_Rectangle__{key}"

                if key == 'id':
                    self.__dict__[key] = val
                elif attr in dics and isinstance(val, int):
                    self.__dict__[f"_Rectangle__{key}"] = val

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        res = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
            }
        return (res)
