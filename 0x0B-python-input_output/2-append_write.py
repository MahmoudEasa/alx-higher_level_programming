#!/usr/bin/python3
"""Module to appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Module to appends a string at the end of a text file (UTF8)
        and returns the number of characters added

        Args:
            filename (str): The file name
            text (str): The text to append in file
    """

    with open(filename, "a") as f:
        nb_char = f.write(text)

    return (nb_char)
