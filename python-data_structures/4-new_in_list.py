#!/usr/bin/python3i
# Replacees an element in a list at a specific position without modifying


def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > (len(new_list) - 1):
        new_list = my_list
        return new_list
    else:
        new_list[idx] = element
        return new_list

