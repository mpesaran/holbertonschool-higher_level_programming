#!/usr/bin/python3
def element_at(my_list, idx):
    if 0<=idx<=len(my_list):
        return my_list[idx]
    return

my_list = [1, 2, 3, 4, 5]
idx = 0
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))