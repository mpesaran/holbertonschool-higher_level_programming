#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if 0<=idx<=len(my_list):
        new_list = my_list[:idx]
        new_list.append(element)
        new_list = new_list+my_list[idx+1:]
        return new_list
    return