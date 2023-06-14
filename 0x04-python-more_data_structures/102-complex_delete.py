#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if type(a_dictionary) == dict:
        found = {}
        for key in a_dictionary:
            if a_dictionary[key] == value:
                found[key] = a_dictionary[key]
        for k in found:
            del a_dictionary[k]

    return (a_dictionary)
