#!/usr/bin/python3
"""
This module is to have a function to check if object is inherited fr.m a 
specified class
"""


def inherits_from(obj, a_class):
    """Returns true if object is inhereted of a_class otherwise false"""
    return isinstance(obj, a_class) and type(obj) is not a_class


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
