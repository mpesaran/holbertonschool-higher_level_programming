#!/usr/bin/python3
"""
This module is to have a class which has an empty method
"""


class BaseGeometry:
    """This class has a method area which raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if the value for name is integer and greter than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
