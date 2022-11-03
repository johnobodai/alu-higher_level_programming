#!/usr/bin/python3
# Computes the square value of all intergers of a matrix


def square_matrix_simple(matrix=[]):
    matcpy = matrix.copy
    matsq = []
    for row in range(len(matrix)):
        k = [i*i for i in matrix[row]]
        matsq.append(k)
    return matsq


'''
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print(square_matrix_simple(matrix))
'''
