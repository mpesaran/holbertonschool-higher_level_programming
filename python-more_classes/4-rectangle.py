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

    def area(self):
        """Calculates area of the rectangle object"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of the rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        result = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                result = result + "#"
            if not i == self.__height - 1:
                result = result + "\n"
        return result

    def __repr__(self):
        """Returns a string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
