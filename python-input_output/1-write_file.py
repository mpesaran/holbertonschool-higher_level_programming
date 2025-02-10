#!/usr/bin/python3
"""This module is about writting to a file"""


def write_file(filename="", text=""):
    """This function writes in a file and returns number of
    characters written in file"""
    with open(filename, 'w', encoding='utf-8') as f:
        chars = f.write(text)
        return chars
