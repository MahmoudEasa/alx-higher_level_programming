#!/usr/bin/python3

"""Class Square that defines a square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """The Initial Attributes

            Attributes:
                __size (int): Private instance attribute
        """

        self.size = size

    @property
    def size(self):
        """Retrieve square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set square"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        else:
            for r in range(self.__size):
                for c in range(self.__size):
                    print("#", end="")
                print()
