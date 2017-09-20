#!/usr/bin/env python3
'''
Bubble sort
'''

def bubble_sort(values):
    '''
    Bubble sort
    '''
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(values)):
            if values[j-1] > values[j]:
                swap = False
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
