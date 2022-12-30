#!/usr/bin/env python3
'''
Insertion sort
'''

def insertion_sort(num_list) :
    '''
    Insertion sort
    '''

    if len(num_list) < 2 :
        return num_list
    for i in range(1, len(num_list)) :
        key = num_list.pop(i)
        j = i-1
        while num_list[j] > key and j >= 0 :
            j -= 1
        num_list.insert(j+1, key)
    return num_list


def test_insertion_sort():
    '''
    Test insertion_sort()
    '''
    data = list(range(1000))
    import random
    random.shuffle(data)
    assert insertion_sort(data) == list(range(1000))
