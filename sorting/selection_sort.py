#!/usr/bin/env python3
'''
Selection sort
'''


def selection_sort(num_list) :
    '''
    Selection sort
    '''

    for i in range(len(num_list)) :
        lowest = num_list[i]
        pos = i
        for j in range(i+1, len(num_list)) :
            if num_list[j] < lowest :
                lowest = num_list[j]
                pos = j
        num_list.insert(i, num_list.pop(pos))
    return num_list


def test_selection_sort():
    '''
    Test selection_sort()
    '''
    data = list(range(1000))
    import random
    random.shuffle(data)
    assert selection_sort(data) == list(range(1000))
