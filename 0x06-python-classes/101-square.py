#!/usr/bin/python3

"""Class Square that defines a square"""


class Square:
    """class Square"""

    def __str__(self):
        """Set Square to have the same behavior as my_print()"""

        self.my_print()
        return ("")

    def __init__(self, size=0, position=(0, 0)):
        """The Initial Attributes

            Attributes:
                __size (int): Private instance attribute
                __position (tuple): Private instance attribute
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Set position"""

        if len(value) == 2 and type(value) == tuple\
                and type(value[0]) == int\
                and type(value[1]) == int\
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for r in range(self.__size):
                print(end=" " * self.__position[0])
                for c in range(self.__size):
                    print("#", end="")
                print()
