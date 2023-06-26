#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_len = 0
    try:
        for el in range(x):
            print(f"{my_list[el]}", end="")
            print_len += 1
    except IndexError:
        return (print_len)
    finally:
        print()

    return (print_len)
