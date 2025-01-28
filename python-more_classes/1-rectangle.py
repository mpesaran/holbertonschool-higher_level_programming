#!/usr/bin/python3
"""This is a rectangle class to define a rectangle"""


class Rectangle:
    """initiates objects and set the height and width"""

    def __init__(self, width=0, height=0):
        """initiate the object with the values given"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("hegiht must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("hegiht must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.height = -4
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.height = "4"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))