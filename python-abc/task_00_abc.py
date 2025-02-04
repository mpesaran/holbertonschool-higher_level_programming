#!/usr/bin/env python3
"""This module is to have an abstract class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """This is an abstract class"""
    @abstractmethod
    def sound(self):
        """This is an abstract method"""
        pass


class Dog(Animal):
    """This one is a child class of abstract class Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """This one is a child class of abstract class Animal"""
    def sound(self):
        return "Meow"
