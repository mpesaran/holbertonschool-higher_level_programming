#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        return float(result)
    except ZeroDivisionError:
        result = None
    finally:
        if result is None:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {:0.1f}".format(result))


a = 11
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))