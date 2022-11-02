#!/usr/bin/python3
# Prints a matrix of integers



def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")

'''
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print_matrix_integer(matrix)
'''
