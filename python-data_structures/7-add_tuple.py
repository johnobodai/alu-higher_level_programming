#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    for i in tuple_a:
        for j in tuple_b:
            if tuple_a.index(j) == tuple_b.index(i):
                k = i + j
                result = result.append(k)
    return tuple(result)


'''
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
'''
