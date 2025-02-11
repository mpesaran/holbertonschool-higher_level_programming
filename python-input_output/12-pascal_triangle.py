#!/usr/bin/python3
"""This module is about a function to create
a Pascal triangle"""


def pascal_triangle(n):
    """Create a Pascal trinagle with n rows"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1]]
    for i in range(1, n):
        item = [1]
        previous_item = triangle[i - 1]
        for j in range(1, len(previous_item)):
            item.append(previous_item[j - 1] + previous_item[j])
        item.append(1)
        triangle.append(item)
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))