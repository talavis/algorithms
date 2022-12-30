#!/usr/bin/env python3
'''
Testing different sorting algorithms
'''

import timeit

for i in (10, 10**2, 10**3, 10**4):
    print('Sort {} random numbers:'.format(i))
    setup = '''
import random
import insertion_sort as ins_sort
import merge_sort as mer_sort
import selection_sort as sel_sort
import bubble_sort as bub_sort

values = list(range({}))
random.shuffle(values)
'''.format(i)

    run = timeit.timeit('ins_sort.insertion_sort(values)', setup=setup, number=1)
    print('Insertion sort: {}'.format(run))
    run = timeit.timeit('sel_sort.selection_sort(values)', setup=setup, number=1)
    print('Selection sort: {}'.format(run))
    run = timeit.timeit('mer_sort.merge_sort(values)', setup=setup, number=1)
    print('Merge sort: {}'.format(run))
    run = timeit.timeit('bub_sort.bubble_sort(values)', setup=setup, number=1)
    print('Bubble sort: {}'.format(run))

