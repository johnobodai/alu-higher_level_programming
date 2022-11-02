#!/usr/bin/python3
# Returns the maximum of a list of numbers


def max_integer(my_list=[]):
    maximum = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > maximum:
                maximum = i
        return maximum


# a = [1, 90, 2, 13, 34, 5, -13, 3]
# print(max_integer(a))
