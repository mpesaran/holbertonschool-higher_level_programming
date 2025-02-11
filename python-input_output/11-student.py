#!/usr/bin/python3
"""This module is about write a class called student"""


class Student:
    """this class has 3 public attributes and one public method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert object to a dictionary"""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of student instance
        with values from the json dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
