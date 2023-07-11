#!/usr/bin/python3
"""Module to adds all arguments to a Python list,
    and then save them to a file
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


arg_len = len(sys.argv)

try:
    load_json = load_from_json_file("add_item.json")
except FileNotFoundError:
    load_json = []

for i in range(arg_len - 1):
    load_json.append(sys.argv[i + 1])

save_to_json_file(load_json, "add_item.json")
