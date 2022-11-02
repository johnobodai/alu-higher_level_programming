#!/usr/bin/python3
# Appends true if divisible by 2 else false


def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
