#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)

    if ta_len == 0:
        tuple_a = (0, 0)
    elif ta_len == 1:
        tuple_a = (1, 0)
    if tb_len == 0:
        tuple_b = (0, 0)
    elif tb_len == 1:
        tuple_b = (1, 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
