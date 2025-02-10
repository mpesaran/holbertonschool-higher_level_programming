#!/usr/bin/python3
"""This module is about append to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file and returns
    number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        chars = f.write(text)
        return chars
