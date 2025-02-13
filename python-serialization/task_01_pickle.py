#!/usr/bin/python3
"""This module is about serializing and deserializing using pickle"""
import pickle


class CustomObject:
    """This clsas is to create a custom class and serialize it later"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays object attributes."""
        for key, value in (self.__dict__).items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        """Serializes the object to a file."""
        with open(filename, 'wb') as f:
            f.write(pickle.dumps(self))

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file."""
        with open(filename, 'rb') as f:
            return pickle.loads(f.read())
