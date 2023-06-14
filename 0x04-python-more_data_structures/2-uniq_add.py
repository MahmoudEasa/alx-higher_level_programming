#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    for i in list(set(my_list)):
        x += i
    return (x)
