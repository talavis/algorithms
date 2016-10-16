#!/usr/bin/env python3

'''
Merge sort
'''


def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q

    L = [0] * (n1+1)
    R = [0] * (n2+1)

    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    sentinel = max(A)+1
    L[n1] = sentinel
    R[n2] = sentinel
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def test_merge():
    A = [1,7,9,3,5,0,2,4,6,8]
    p = 0
    q = 2
    r = 4
    merge(A, p, q, r)
    assert A == [1,3,5,7,9,0,2,4,6,8]
    A = [1,7,9,3,5,0,2,4,6,8]
    p = 3
    q = 4
    r = 5
    merge(A, p, q, r)
    assert A == [1,7,9,0,3,5,2,4,6,8]


def merge_alt(A, p, q, r):
    '''
    Alternative version of merge, using no sentinels
    '''
    n1 = q-p+1
    n2 = r-q

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            if i == n1:
                A[k+1:r+1] = R[j:]
                break
        else:
            A[k] = R[j]
            j += 1
            if j == n2:
                A[k+1:r+1] = L[i:]
                break


def test_merge_alt():
    A = [1,7,9,3,5,0,2,4,6,8]
    p = 0
    q = 2
    r = 4
    merge_alt(A, p, q, r)
    assert A == [1,3,5,7,9,0,2,4,6,8]
    A = [1,7,9,3,5,0,2,4,6,8]
    p = 3
    q = 4
    r = 5
    merge_alt(A, p, q, r)
    assert A == [1,7,9,0,3,5,2,4,6,8]


def merge_helper(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_helper(A, p, q)
        merge_helper(A, q+1, r)
        merge(A, p, q, r)


def merge_sort(A):
    merge_helper(A, 0, len(A)-1)


def test_merge_sort():
    import random

    A = [4, 0, 3, 2, 1]
    merge_sort(A)
    assert A == sorted(A)

    A = list(range(1000))
    random.shuffle(A)
    merge_sort(A)
    assert A == sorted(A)
