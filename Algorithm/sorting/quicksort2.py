#!/bin/python
def quickSort(ar):    
    if len(ar) <= 1:
        return ar
    else:
        pivot = ar[0]
        less = [i for i in ar if i < pivot]
        equal = [i for i in ar if i == pivot]
        greater = [i for i in ar if i > pivot]
        res = quickSort(less) + equal + quickSort(greater)
        print ' '.join([str(i) for i in res])
        return res

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)