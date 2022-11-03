#!/usr/bin/python3
# Replaces all occurrences of an element by another in a new list

def search_replace(my_list, search, replace):
    newlist = []
    newlist = [replace if i == search else i for i in my_list]
    return newlist


'''
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
print(search_replace(my_list, 2, 89))
'''
