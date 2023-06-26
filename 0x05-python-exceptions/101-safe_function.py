#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (IndexError, TypeError, ValueError, ZeroDivisionError) as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(err))
        sys.stderr.write("\n")
        return (None)
