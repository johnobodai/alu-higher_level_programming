#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    result = [x+y for x in list_a for y in list_b if list_a.index(x) == list_b.index(y)]
    print(tuple(result))

tuple_a = (1, 89)
tuple_b = (88, 11)
add_tuple(tuple_a, tuple_b)


