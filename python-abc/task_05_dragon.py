#!/usr/bin/env python3
"""This module is about Mixins"""


class SwimMixin:
    """Swimmixin class"""
    def swim(self):
        """Creature swims"""
        print("The creature swims!")


class FlyMixin:
    """Flymixin class"""
    def fly(self):
        """Creature flies"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """This is dragon class inherited fron
    swimmixin and flymixin classes"""
    def roar(self):
        """This dragon roars"""
        print("The dragon roars!")
