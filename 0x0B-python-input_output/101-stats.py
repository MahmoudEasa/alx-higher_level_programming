#!/usr/bin/python3
"""Module to reads stdin line by line and computes metrics
"""


file_size = 0
lines = 0
status_obj = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
        }


def print_status():
    """Function to print result
    """
    print(f"File size: {file_size}")
    for status in list(status_obj.keys()):
        if status_obj[status] > 0:
            print(f"{status}: {status_obj[status]}")


try:
    while True:
        input_str = input()
        lines += 1
        if lines == 10:
            print_status()
            lines = 1
        print(lines)
        if len(input_str):
            inputs = input_str.split(" ")
            file_size += int(inputs[-1])
            st = int(inputs[-2])
            for status in list(status_obj.keys()):
                if st == status:
                    status_obj[status] += 1
                    break
except KeyboardInterrupt:
    print_status()
