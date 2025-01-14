#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} argument.".format(argc))
    else:
        print("{} arguments:".format(argc))
    i = 1
    for arg in argv:
        print("{}: {}".format(i, arg))
        i += 1
