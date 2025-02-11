#!/usr/bin/python3
"""This module is about to connvert an instance of a class to a dictionary"""


def class_to_json(obj):
    """Returns the dictionary description of an instance of a class"""
    return obj.__dict__
