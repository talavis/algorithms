#!/usr/bin/env python3
'''
Bisection search
'''

def bisect_search_rec(sort_list, target):
    '''
    Find a target value in a sorted list.
    Recursive approach.
    sort_list - a sorted list
    target - the wanted value
    '''
    def helper(sort_list, target, low, high):
        '''
        Helper for bisect search
        '''
        if low == high:
            return sort_list[low] == target
        mid = (low + high)//2
        if sort_list[mid] == target:
            return True
        if sort_list[mid] > target:
            if low == mid:
                return False
            return helper(sort_list, target, low, mid-1)
        return helper(sort_list, target, mid+1, high)

    if not sort_list:
        return False
    return helper(sort_list, target, 0, len(sort_list)-1)
