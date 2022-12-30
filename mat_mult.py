#!/usr/bin/env python3

'''
Matrix multiplication
'''


def matrix_multiply(mat_a, mat_b):
    '''
    Multiply two n*n matrices
    '''
    n = len(mat_a)
    result =  [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat_a[i][k]*mat_b[k][j]
                print(result)

    return result


def test_matrix_multiply():
    '''
    Test matrix_multiply
    '''
    mat_a = [[1, 2], [3, 4]]
    mat_b = [[2, 0], [1, 2]]
    result = [[4, 4], [10, 8]]
    assert matrix_multiply(mat_a, mat_b) == result


