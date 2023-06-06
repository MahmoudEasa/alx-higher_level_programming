#!/usr/bin/python3
def uppercase(str):
    str_len = len(str)
    for i, c in enumerate(str):
        end_chr = "\n" if i == str_len - 1 else ""
        if ord(c) in range(ord('a'), ord('z') + 1):
            char = chr(ord(c) - 32)
            print("{}".format(char), end=end_chr)
        else:
            print("{}".format(c), end=end_chr)
