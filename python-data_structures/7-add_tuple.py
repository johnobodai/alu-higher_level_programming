#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    for i in list(tuple_a):                               
        for j in list(tuple_b):
            if list(tuple_a).index(j) == list(tuple_b).index(i):
                k = i + j
                result = list().append(k)
        print(result)


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

