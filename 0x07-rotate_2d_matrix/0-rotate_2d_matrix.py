#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it
90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must
be edited in-place.
You can assume the matrix will have
2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
 