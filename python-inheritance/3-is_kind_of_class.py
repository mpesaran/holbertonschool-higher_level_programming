#!/usr/bin/python3
"""
This module is to have a function to chaeck if function is an instance of
specified class or its subclasses
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obje is instance of a_class otherwise false"""
    return isinstance(obj, a_class)
