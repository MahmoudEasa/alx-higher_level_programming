#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("0")
    else:
        add = 0
        for i in range(argv_len - 1):
            add += int(sys.argv[i + 1])
        print("{}".format(add))
