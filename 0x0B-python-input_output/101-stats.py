#!/usr/bin/python3

"""Module to reads
    stdin line by line and computes metrics

    Input format: <IP Address> - [<date>]
        "GET /projects/260 HTTP/1.1"
        <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C),
        prints those statistics since the beginning:
    Total file size: File size: <total size>
    where is the sum of all previous (see input format above)
    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    if a status code doesn’t appear,
        don’t print anything for this status code
    format: <status code>: <number>
    status codes should be printed in ascending order

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
