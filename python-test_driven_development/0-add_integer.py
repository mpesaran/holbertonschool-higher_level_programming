#!/usr/bin/python3
"""
This module provides a function `add_integer(a, b=98)` to add two numbers.
"""


def add_integer(a, b=98):
    ''' Adds two integers or floats, casting them to integers if necessary.
    Raises:
        TypeError: If a or b is not an integer or float.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
