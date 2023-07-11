#!/usr/bin/python3
"""Module to reads a text file (UTF8) and prints it to stdout

"""


def read_file(filename=""):
    """Function to reads a text file (UTF8) and prints it to stdout

        Args:
            filename (str): the file name
    """

    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
