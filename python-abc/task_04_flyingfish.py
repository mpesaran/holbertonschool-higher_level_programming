#!/usr/bin/env python3
"""This module is about multiple inheritance"""

class Fish:
    """This is class Fish"""
    def swim(self):
        """fish swims"""
        print("The fish is swimming")

    def habitat(self):
        """fish is a habitat"""
        print("The fish lives in water")


class Bird:
    """This is bird class"""
    def fly(self):
        """Birds fly"""
        print("The bird is flying")

    def habitat(self):
        """bird is a habitat"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Flyfish is both fish and bird"""
    def fly(self):
        """flyfish flies"""
        print("The flying fish is soaring!")

    def swim(self):
        """flyfish swims"""
        print("The flying fish is swimming!")

    def habitat(self):
        """flyfish is a habitat too"""
        print("The flying fish lives both in water and the sky!")
