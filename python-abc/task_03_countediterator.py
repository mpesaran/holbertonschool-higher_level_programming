#!/usr/bin/env python3
"""This module is to extend built-in classes to add
or modify behavior"""


class CountedIterator:
    """An iterator wrapper that counts the number
    of iterations."""
    def __init__(self, obj):
        self._object_itr = iter(obj)
        self._counter = 0

    def get_count(self):
        """eturn the current count of items iterated."""
        return self._counter

    def __next__(self):
        try:
            value = next(self._object_itr)
            self._counter += 1
            return value
        except StopIteration:
            raise StopIteration
