#!/usr/bin/env python3
'''
Merge sort
'''


def merge(values, low, mid, high):
    '''
    Merge sort
    '''
    len1 = mid-low+1
    len2 = high-mid

    left = [0] * (len1+1)
    right = [0] * (len2+1)

    for i in range(len1):
        left[i] = values[low+i]
    for j in range(len2):
        right[j] = values[mid+j+1]
    sentinel = max(values)+1
    left[len1] = sentinel
    right[len2] = sentinel
    i = 0
    j = 0
    for k in range(low, high+1):
        if left[i] <= right[j]:
            values[k] = left[i]
            i += 1
        else:
            values[k] = right[j]
            j += 1


def test_merge():
    '''
    Test merge_sort()
    '''
    values = [1, 7, 9, 3, 5, 0, 2, 4, 6, 8]
    low = 0
    mid = 2
    high = 4
    merge(values, low, mid, high)
    assert values == [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    values = [1, 7, 9, 3, 5, 0, 2, 4, 6, 8]
    low = 3
    mid = 4
    high = 5
    merge(values, low, mid, high)
    assert values == [1, 7, 9, 0, 3, 5, 2, 4, 6, 8]


def merge_alt(values, low, mid, high):
    '''
    valueslternative version of merge, using no sentinels
    '''
    len1 = mid-low+1
    len2 = high-mid

    left = [0] * (len1)
    right = [0] * (len2)

    for i in range(len1):
        left[i] = values[low+i]
    for j in range(len2):
        right[j] = values[mid+j+1]
    i = 0
    j = 0
    for k in range(low, high+1):
        if left[i] <= right[j]:
            values[k] = left[i]
            i += 1
            if i == len1:
                values[k+1:high+1] = right[j:]
                break
        else:
            values[k] = right[j]
            j += 1
            if j == len2:
                values[k+1:high+1] = left[i:]
                break


def test_merge_alt():
    '''
    Test merge_alt()
    '''
    values = [1, 7, 9, 3, 5, 0, 2, 4, 6, 8]
    low = 0
    mid = 2
    high = 4
    merge_alt(values, low, mid, high)
    assert values == [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    values = [1, 7, 9, 3, 5, 0, 2, 4, 6, 8]
    low = 3
    mid = 4
    high = 5
    merge_alt(values, low, mid, high)
    assert values == [1, 7, 9, 0, 3, 5, 2, 4, 6, 8]


def merge_sort(values):
    '''
    Recursive version of merge sort
    '''
    def merge_helper(values, low, high):
        '''
        Merge sort helper
        '''
        if low < high:
            mid = (low + high)//2
            merge_helper(values, low, mid)
            merge_helper(values, mid+1, high)
            merge(values, low, mid, high)

    merge_helper(values, 0, len(values)-1)


def general_test(sort_func):
    '''
    General function for testing sorts
    '''
    import random

    testdata = [4, 0, 3, 2, 1]
    sort_func(testdata)
    if not testdata == sorted(testdata):
        return False

    testdata = list(range(1000))
    random.shuffle(testdata)
    sort_func(testdata)
    if not testdata == sorted(testdata):
        return False

    testdata = list(range(500))*2
    random.shuffle(testdata)
    sort_func(testdata)
    if not testdata == sorted(testdata):
        return False
    return True


def test_merge_sort_rec():
    '''
    Test merge_sort_rec()
    '''
    assert general_test(merge_sort)
