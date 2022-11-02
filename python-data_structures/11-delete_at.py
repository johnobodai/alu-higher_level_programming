#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        my_list = [i for i in my_list if i != my_list(i)]
        return my_list
