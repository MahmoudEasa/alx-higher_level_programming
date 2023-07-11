#!/usr/bin/python3
"""Module to writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Module to writes a string to a text file (UTF8)
        and returns the number of characters written

        Args:
            filename (str): The file name
            text (str): The text to write in file
    """

    with open(filename, "w") as f:
        nb_char = f.write(text)

    return (nb_char)
