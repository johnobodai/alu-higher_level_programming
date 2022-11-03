#!/usr/bin/python3
# Adds all unique intergers in a list


def uniq_add(my_list=[]):
    j = list(set(my_list))
    sum_ = 0
    for i in j:
        sum_ += i
    return sum_


'''
my_list = [1, 2, 3, 1, 4, 2, 5]
print(uniq_add(my_list))
'''
