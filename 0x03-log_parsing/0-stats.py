#!/usr/bin/python3
"Log parsing"
import re
import sys


def print_data(file_size, status_codes):
    "Print the statistics"
    print(f"File size: {file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}", flush=True)


def main():
    file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for i, line in enumerate(sys.stdin):
            if i != 0 and i % 10 == 0:
                print_data(file_size, status_codes)

            line = line.rstrip()
            pattern = r"""
                [\d.]+
                \s-\s
                \[[\d\- :.]+\]
                \s"GET\s\/projects\/260\sHTTP\/1\.1"\s
                (\d{3})
                \s(\d+)
            """
            res = re.search(pattern, line, re.X)
            code, size = res.groups()
            if code in status_codes:
                file_size += int(size)
                status_codes[code] = status_codes.get(code, 0) + 1
    except (KeyboardInterrupt, EOFError):
        print_data(file_size, status_codes)


if __name__ == "__main__":
    main()
