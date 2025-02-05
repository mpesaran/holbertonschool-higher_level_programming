#!/usr/bin/env python3
"""This module is to extend built-in classes to add
or modify behavior"""


class VerboseList(list):
    """This is an extended class for list type"""
    def append(self, item):
        print(f"Added [{item}] to the list.")
        return super().append(item)

    def extend(self, iterable):
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        return super().remove(value)
