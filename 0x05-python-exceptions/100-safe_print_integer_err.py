#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(err))
        sys.stderr.write("\n")
        sys.stderr.flush()
        return (False)
