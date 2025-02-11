#!/usr/bin/python3
"""This module is about write a class called student"""


class Student:
    """this class has 3 public attributes and one public method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """convert object to a dictionary"""
        return self.__dict__
