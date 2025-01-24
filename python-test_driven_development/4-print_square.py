#!/usr/bin/python3
"""
prints a square of # in size of size
"""


def print_square(size):
    """ Prints a square of '#' characters with the given size."""
    if size is None:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
