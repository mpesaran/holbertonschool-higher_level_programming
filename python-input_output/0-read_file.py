#!/usr/bin/python3
"""This module is about reading from a file"""


def read_file(filename=""):
    """This function will open a text file and read it and close it"""
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end="")
