#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    str_len = len(str)
    str_copy = []
    for i, c in enumerate(str):
        if i != n:
            str_copy.append(c)
    str_copy = "".join(str_copy)
    return (str_copy)
