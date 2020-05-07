#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for j in (matrix):
            new_matrix.append([i ** 2 for i in j])
    return new_matrix
