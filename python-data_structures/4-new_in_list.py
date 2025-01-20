#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if 0 <= idx < len(my_list):
        new_list = my_list[:idx]
        new_list.append(element)
        new_list = new_list+my_list[idx+1:]
        return new_list
    return my_list


my_list = [1, 2, 3]
idx = 3
new_element = 4
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)