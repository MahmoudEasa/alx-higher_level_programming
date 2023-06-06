#!/usr/bin/python3
for i in range(0, 100):
    print("{}{}".format(0 if i < 10 else "", i), end=", " if i < 99 else "\n")
