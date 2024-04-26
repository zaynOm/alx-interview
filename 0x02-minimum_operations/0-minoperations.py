#!/usr/bin/python3
"Minimum Operations"


def minOperations(n):
    "calculate the fewest number of operations needed to result in exactly n H"
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
