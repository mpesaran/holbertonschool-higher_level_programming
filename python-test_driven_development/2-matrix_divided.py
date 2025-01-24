#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number and returns a new matrix.
"""

def matrix_divided(matrix, div):
    ''' This function is to divide numbers in a matrix to a number and return a new matrix'''
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(el / div, 2) for el in row] for row in matrix]
