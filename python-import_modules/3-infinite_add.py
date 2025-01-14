#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    sum = 0
    for num in argv:
        sum += int(num)
    print("{}".format(sum))
