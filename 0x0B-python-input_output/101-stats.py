#!/usr/bin/python3

"""Module to reads stdin line by line and computes metrics

"""


def print_status(file_size, status_obj):
    """Function to print result

        Args:
            file_size (int): The file size
            status_obj (object): The object
    """
    print(f"File size: {file_size}")
    for status in list(status_obj.keys()):
        if status_obj[status] > 0:
            print(f"{status}: {status_obj[status]}")


if __name__ == "__main__":
    import sys

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
                500: 0
            }

    try:
        for line in sys.stdin:
            if lines == 10:
                print_status(file_size, status_obj)
                lines = 1
            else:
                lines += 1

            inputs = line.split()

            input_size = inputs[-1]
            input_stats = inputs[-2]

            if not input_size.isdigit() or not input_stats.isdigit():
                raise ValueError

            file_size += int(input_size)
            st = int(input_stats)

            for status in list(status_obj.keys()):
                if st == status:
                    status_obj[status] += 1
                    break
        print_status(file_size, status_obj)
    except KeyboardInterrupt:
        print_status(file_size, status_obj)
        raise
