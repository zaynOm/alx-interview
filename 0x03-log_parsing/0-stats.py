#!/usr/bin/python3
"Log parsing"
import re
import sys
import signal

file_size = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_data():
    "Print the statistics"
    print(f"File size: {file_size}")
    for code, count in sorted(status_code.items()):
        print(f"{code}: {count}")


def signal_handler(signal, frame):
    "Handle keyboard interruption"
    print_data()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin):
        if i != 0 and i % 10 == 0:
            print_data()

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
        if code in status_code:
            file_size += int(size)
            status_code[code] = status_code.get(code, 0) + 1
except KeyboardInterrupt:
    signal_handler(signal.SIGINT, None)
    raise
