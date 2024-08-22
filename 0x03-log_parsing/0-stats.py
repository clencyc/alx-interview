#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys


def print_stats(file_size, status_codes):
    """
    Prints statistics at the beginning and every 10 lines.
    Also called on Keyboard interruption.
    """
    print("File size:", file_size)
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(code + ":", status_codes[code])


if __name__ == "__main__":
    line_num = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            line_num += 1
            split_line = line.split()

            if len(split_line) > 1:
                file_size += int(split_line[-1])

            if len(split_line) > 2 and split_line[-2].isnumeric():
                status_code = split_line[-2]
            else:
                status_code = "0"

            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_num % 10 == 0:
                print_stats(file_size, status_codes)

        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise