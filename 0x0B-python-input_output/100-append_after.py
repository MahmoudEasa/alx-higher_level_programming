#!/usr/bin/python3
"""Module to inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Function append_arter

        Args:
            filename (str): The file name
            search_string (str): The string to insert after
            new_strign (str): The string to insert
    """

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
