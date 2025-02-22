#!/usr/bin/python3
"""
This module is to have a class which has an empty method
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class initiates a rectangle object"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    # def area(self):
    #     super().area()


r = Rectangle(3, 5)
print(r.area())
