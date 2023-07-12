#!/usr/bin/python3

"""Module to reads stdin line by line and computes metrics

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys


def print_status(file_size, status_obj):
    """Function to print result

    """
    print(f"File size: {file_size}")
    for status in list(status_obj.keys()):
        if status_obj[status] > 0:
            print(f"{status}: {status_obj[status]}")


def main():
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

    try:
        for line in sys.stdin:
            if lines == 10:
                print_status(file_size, status_obj)
                lines = 1
            else:
                lines += 1
            if len(line):
                inputs = line.split()

                try:
                    file_size += int(inputs[-1])
                    st = int(inputs[-2])
                except (ValueError, TypeError):
                    pass

                for status in list(status_obj.keys()):
                    if st == status:
                        status_obj[status] += 1
                        break
    except KeyboardInterrupt:
        print_status(file_size, status_obj)
        raise


if __name__ == "__main__":
    main()
