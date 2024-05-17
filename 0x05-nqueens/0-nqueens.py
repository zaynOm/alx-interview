#!/usr/bin/python3
"""N queens problem"""


import sys


def define_solutions(row, column):
    solutions = [[]]
    for queen in range(row):
        solutions = position_queen(queen, column, solutions)
    return solutions


def position_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():

    n = init()
    # define all solutions
    solutions = define_solutions(n, n)
    # print the solutions
    for array in solutions:
        clean_board = []
        for q, x in enumerate(array):
            clean_board.append([q, x])
        print(clean_board)


# invoking the script directelly
if __name__ == "__main__":
    n_queens()
