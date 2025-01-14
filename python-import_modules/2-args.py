#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    print("{} arguments:".format(argc))
    i = 1
    for arg in argv:
        print("{} : {}".format(i, arg))
        i += 1
