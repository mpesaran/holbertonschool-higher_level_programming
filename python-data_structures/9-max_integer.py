#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if len(my_list) == 0:
        return None
    for i in range(1, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max
