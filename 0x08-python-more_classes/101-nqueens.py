#!/usr/bin/python3
import sys

"""Module to solves the N queens problem
"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

num = sys.argv[1]

if not num.isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

    
