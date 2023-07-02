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

    for i in range(len(text)):
        if text[i] == " " and text[i-1] in [".", "?", ":"]:
            continue
        if text[i] == ".":
            print(".\n")
        elif text[i] == "?":
            print("?\n")
        elif text[i] == ":":
            print(":\n")
        else:
            print(text[i], end="")
