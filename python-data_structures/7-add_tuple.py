#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    result = [x+y for x in list_a[:2] for y in list_b[:2] if list_a.index(x) == list_b.index(y)]
    return (tuple(result))

'''
tuple_a = (1, 2)
tuple_b = (1, 2)
add_tuple(tuple_a, tuple_b)
'''

