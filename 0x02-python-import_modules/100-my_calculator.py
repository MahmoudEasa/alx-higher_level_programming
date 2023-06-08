#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()
argv_len = len(sys.argv)

if argv_len != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

operator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

result = operator.get(sys.argv[2], "not found")
if result == "not found":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(sys.argv[1])
op = sys.argv[2]
b = int(sys.argv[3])

print("{} {} {} = {}".format(a, op, b, result(a, b)))
