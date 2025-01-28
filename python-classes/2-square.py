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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
