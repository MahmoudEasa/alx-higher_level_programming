#!/usr/bin/python3
import sys
argv_len = len(sys.argv)
if __name__ == "__main__":
    if argv_len == 1:
        print("0 arguments.")
    else:
        argument = "argument" if argv_len == 2 else "arguments"
        print("{} {}:".format((argv_len - 1), argument))
        for i in range(argv_len - 1):
            print("{}: {}".format(i + 1, sys.argv[(i + 1)]))
