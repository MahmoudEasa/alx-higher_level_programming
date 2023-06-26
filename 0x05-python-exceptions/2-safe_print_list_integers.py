#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_len = 0
    try:
        for el in range(x):
            if type(my_list[el]) == int:
                print("{:d}".format(my_list[el]), end="")
                print_len += 1
        print()
        return (print_len)
    except IndexError:
        raise
