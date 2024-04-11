#!/usr/bin/python3
"Pascals triangle implementation"


def pascal_triangle(n):
    "show me that triangle"
    if n <= 0:
        return []

    array = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 1:
                row.append(array[i - 1][j] + array[i - 1][j - 1])
        array.append(row)

    return array
