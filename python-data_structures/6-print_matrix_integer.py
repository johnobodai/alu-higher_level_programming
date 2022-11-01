#!/usr/bin/python3
# Prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for i in matrix:      
        for j in i:
            print("{:d}".format(j),end=' ')
        print('\n',end='')


'''
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print_matrix_integer(matrix)
'''
