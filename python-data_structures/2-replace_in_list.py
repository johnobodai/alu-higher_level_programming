#!/usr/bin/python3
# Replace an element of a list at a specific position
# @idx is the index to be replaced
# @element is the new element to replace the element at index

def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list


# a = [1, 2, 3]
# replace_in_list(a, 1, 4)

# print(replace_in_list(a, 1, 4))
