#!/usr/bin/python3
"""
This module is to have a class which has an empty method
"""


class BaseGeometry:
    """This class has a method area which raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
