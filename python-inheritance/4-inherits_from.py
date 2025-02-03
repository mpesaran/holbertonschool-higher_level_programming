#!/usr/bin/python3
"""
This module is to have a function to check if object is inherited fr.m a
specified class
"""


def inherits_from(obj, a_class):
    """Returns true if object is inhereted of a_class otherwise false"""
    return isinstance(obj, a_class) and type(obj) is not a_class
