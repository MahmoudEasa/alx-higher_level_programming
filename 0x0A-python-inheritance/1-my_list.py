#!/usr/bin/python3

"""Module to Write a class MyList that inherits from list

"""


class MyList(list):

    """Class inherits from list

        Args:
            list (list): the list class

    """

    def print_sorted(self):
        """Function ot print sorted list

        """
        if len(self):
            print(sorted(self))
        else:
            print("[]")
