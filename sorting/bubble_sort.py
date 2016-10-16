#!/usr/bin/env python3
'''
Bubble sort
'''

def bubble_sort(values) :
    '''
    Bubble sort
    '''
    for i in range(len(values)-1):
        for j in range(len(values)-1, i, -1):
            if values[j] < values[j-1]:
                tmp = values[j]
                values[j] = values[j-1]
                values[j-1] = tmp


def test_bubble_sort():
    '''
    Test bubble_sort()
    '''
    data = list(range(1000))
    import random
    random.shuffle(data)
    bubble_sort(data)
    assert data == list(range(1000))
