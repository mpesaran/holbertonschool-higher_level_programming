#!/usr/bin/env python3
"""This module is to have an abstract class"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """This is an abstract class"""
    @abstractmethod
    def area(self):
        """This is an abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """This is an abstrat method to calculate perimeter"""
        pass


class Circle(Shape):
    """This one is a child class of abstract class Animal"""
    def __init__(self, radius):
        super().__init__()
        self.__radius = abs(radius)

    def perimeter(self):
        return 2 * self.__radius * math.pi

    def area(self):
        return (self.__radius ** 2) * math.pi


class Rectangle(Shape):
    """This one is a child class of abstract class Animal"""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def area(self):
        return self.__height * self.__width


def shape_info(sh):
    """A function to call perimeter and area methods regardless of
    objects actual class
    """
    print(f"Area: {sh.area()}")
    print(f"Perimeter: {sh.perimeter()}")
