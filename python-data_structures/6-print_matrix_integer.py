#!/usr/bin/python3
# Prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print('{:d}'.format(i), end='')
