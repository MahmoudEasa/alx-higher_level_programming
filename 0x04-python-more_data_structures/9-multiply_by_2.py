#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, i in a_dictionary.items():
        new_dict[k] = (i * 2)
    return (new_dict)
