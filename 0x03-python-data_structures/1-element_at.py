#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)

    if idx < 0 or idx >= list_len:
        return (None)

    for i in range(list_len):
        if i == idx:
            return (my_list[i])
