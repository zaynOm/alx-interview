#!/usr/bin/python3
import re
import sys


def print_data(file_size, status_codes):
    print(f"File size: {file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


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
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
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
            if res:
                code, size = res.group(1), int(res.group(2))
                if code in status_codes:
                    file_size += size
                    status_codes[code] += 1
            if line_count % 10 == 0:
                print_data(file_size, status_codes)
    except KeyboardInterrupt:
        print_data(file_size, status_codes)


if __name__ == "__main__":
    main()
