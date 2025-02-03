#!/usr/bin/python3
"""
This module is to have a function to chaeck if function is an instance of
specified class
"""


def is_same_class(obj, a_class):
    """Returns true if obje is instance of a_class otherwise false"""
    if isinstance(obj, a_class):
        return True
    return False
