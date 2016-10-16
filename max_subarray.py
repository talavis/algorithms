#!/usr/bin/env python3
'''
Find the highest-scoring subarray
'''

import sys


def find_max_crossing_subarray(A, low, mid, high):
    '''
    Find the highest-scoring part from the middle of the subarray
    '''
    sent = min(A) - 1

    left_sum = sent
    curr_sum = 0
    for i in range(mid, low-1, -1):
        curr_sum += A[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
            max_left = i

    right_sum = sent
    curr_sum = 0
    for i in range(mid+1, high+1):
        curr_sum += A[i]
        if curr_sum > right_sum:
            right_sum = curr_sum
            max_right = i
    
    return (max_left, max_right, left_sum + right_sum)


def test_find_max_crossing_subarray():
    '''
    Test find_max_crossing_subarray()
    '''
    data = [-1, -2, 5, 6, 7, 0, -1]
    assert find_max_crossing_subarray(data, 0, 3, 6) == (2, 4, 18)
    assert find_max_crossing_subarray(data, 0, 1, 3) == (1, 3, 9)
    data = [13, -3, -25, 20, -3, -16, -23, 18,
            20, -7, 12, -5, -22, 15, -4, -7]
    assert find_max_crossing_subarray(data, 0, 7, 15) == (7, 10, 43)
    assert find_max_crossing_subarray(data, 2, 3, 4) == (3, 4, 17)


def find_max_subarray_helper(A, low, high):
    '''
    Find the highest-scoring subarray.
    Handles the recursion
    '''
    if low == high:
        return (low, high, A[low])
    mid = (low + high) // 2
    left= find_max_subarray_helper(A, low, mid)
    right = find_max_subarray_helper(A, mid+1, high)
    cross = find_max_crossing_subarray(A, low, mid, high)
    if left[2] >= right[2] and left[2] >= cross[2]:
        return left
    elif right[2] >= left[2] and right[2] >= cross[2]:
        return right
    else:
        return cross


def test_find_max_subarray_helper():
    '''
    Test find_max_subarray
    '''
    data = [13, -3, -25, 20, -3, -16, -23, 18,
            20, -7, 12, -5, -22, 15, -4, -7]
    assert find_max_subarray_helper(data, 0, 15) == (7, 10, 43)
    assert find_max_subarray_helper(data, 0, 3) == (3, 3, 20)


def find_max_subarray(A):
    '''
    Find the highest-scoring subarray.
    '''
    return find_max_subarray_helper(A, 0, len(A)-1)


def test_find_max_subarray():
    '''
    Test find_max_subarray
    '''
    data = [-1, -2, 5, 6, 7, 0, -1]
    assert find_max_subarray(data) == (2, 4, 18)
    data = [13, -3, -25, 20, -3, -16, -23, 18,
            20, -7, 12, -5, -22, 15, -4, -7]
    assert find_max_subarray(data) == (7, 10, 43)
