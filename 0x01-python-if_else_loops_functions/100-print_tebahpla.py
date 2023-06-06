#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    char = chr(i) if i % 2 == 0 else chr(i - 32)
    print("{}".format(char), end="")
