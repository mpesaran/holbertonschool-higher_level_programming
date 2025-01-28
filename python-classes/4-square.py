#!/usr/bin/python3
"""
This module defines the Square class with attribute.
"""


class Square:
    """Represents a square with private size attributes."""
    def __init__(self, size=0):
        """
        Initialize the square with an optional.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
