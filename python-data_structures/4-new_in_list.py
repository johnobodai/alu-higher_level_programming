#!/usr/bin/python3i
# Replacees an element in a list at a specific position without modifying


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return new_list
    else:
        new_list[idx] = element
        return new_list

# my_list = [1, 2, 3]
# print(new_in_list(my_list, 1, 4))
# print(my_list)
'''
def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list
'''
