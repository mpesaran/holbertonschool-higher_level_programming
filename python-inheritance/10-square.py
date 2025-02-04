#!/usr/bin/python3
"""
This module is to have a class which has an empty method
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class initiates a square object"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates area of the rectangle"""
        return self.__size ** 2
