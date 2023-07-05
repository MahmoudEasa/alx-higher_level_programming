#!/usr/bin/python3

"""Module to print a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Function to print a text

        Args:
            text (str): string
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    text_len = len(text)

    found = 0

    for i in range(text_len):
        if found and text[i] == " ":
            continue
        if text[i] == ".":
            print(".\n")
            found = 1
        elif text[i] == "?":
            print("?\n")
            found = 1
        elif text[i] == ":":
            print(":\n")
            found = 1
        else:
            print(text[i], end="")
            found = 0
