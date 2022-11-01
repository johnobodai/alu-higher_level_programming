#!/usr/bin/python3
# Prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for i, j, k in i:
            print('{:d} {:d} {:d}'.format(i, j, k))
