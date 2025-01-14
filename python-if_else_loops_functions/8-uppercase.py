#!/usr/bin/python3
def uppercase(str):
    result = ""
    for a in str:
        if ord(a) > 96 and ord(a) < 123:
            result += chr(ord(a) - 32)
        else:
            result += a
    print("{}".format(result), end="")
    print("")
