#!/usr/bin/python3
def remove_char_at(str, n):
    str_len = len(str)
    if n < 0:
        n = str_len - -n
    str_copy = []
    for i, c in enumerate(str):
        if i != n:
            str_copy.append(c)
    str_copy = "".join(str_copy)
    return (str_copy)
