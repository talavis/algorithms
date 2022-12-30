#!/usr/bin/env python3
def flatten(item):
    ''' 
    item: an item, potentially a list
    Returns a flattened list of all items
    '''
    outlist = []
    if type(aList) is list:
        for item in aList:
            outlist.extend(flatten(item))
    else:
        outlist.append(aList)
    return outlist
