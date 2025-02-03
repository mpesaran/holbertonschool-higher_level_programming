#!/usr/bin/python3
"""
This module defines a new class which inherits list type
"""


class Mylist(list):
    """new class that is a child of list class"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
