#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        if a is None:
            raise ValueError
        if not isinstance(b, int):
            raise TypeError
        if isinstance(a, float) or isinstance(a, float):
            a = int(a)
            b = int(b)
        return  a + b
    except TypeError:
        print("b must be an integer")
    except ValueError:
        print("a must be an integer")
