#!/usr/bin/python3
"""
prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    ''' This function is to print out first name and last name'''
    if first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
