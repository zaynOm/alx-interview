#!/usr/bin/python3
"""Rotate a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90° clockwise"""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
