#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)

    if idx < 0 or idx >= list_len:
        return (my_list)

    for i in range(list_len):
        if i == idx:
            del my_list[i]

    return (my_list)
