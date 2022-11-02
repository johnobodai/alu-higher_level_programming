#!/usr/bin/python3


def max_integer(my_list=[]):
    maximum = my_list[0]
    for i in my_list:
        if i > maximum:
            maximum = i
    return maximum



# a = [1, 90, 2, 13, 34, 5, -13, 3]
# print(max_integer(a))
