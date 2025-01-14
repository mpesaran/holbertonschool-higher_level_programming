#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) > 96 and ord(a) < 123:
            a = ord(a) - 32
            print("{}".format(chr(a)), end="")
        else:
            print("{}".format(a), end="")
    print("")


