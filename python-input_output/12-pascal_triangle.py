#!/usr/bin/python3
"""This module is about a function to create
a Pascal triangle"""


def pascal_triangle(n):
    """Create a Pascal trinagle with n rows"""
    triangle = []
    item = []
    if n <= 0:
        return []
    if n == 1:
        triangle.append([1])

    for i in range(1, n):
        item = [1]
        previous_item = triangle[i - 1]
        for j in range(1, n):
            item.append(item.append(previous_item[j - 1] + previous_item[j]))
        item.append(1)
        triangle.append(item)
    return triangle
