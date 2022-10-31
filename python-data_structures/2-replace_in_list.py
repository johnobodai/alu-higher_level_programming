#!/usr/bin/python3


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
