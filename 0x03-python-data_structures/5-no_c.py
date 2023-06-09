#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    str_len = len(my_string)

    if str_len > 0:
        for i in range(str_len):
            if my_string[i] != 'c' and my_string[i] != 'C':
                new_str += my_string[i]

    return (new_str)
