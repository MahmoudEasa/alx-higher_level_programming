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

    for i in range(text_len):
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

        if i == (text_len - 1) and text[i] not in ['.', ':', '?']:
            print()
