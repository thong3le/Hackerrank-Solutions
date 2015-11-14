#!/bin/python
def partition(ar):    
    p = ar[0]
    left = [i for i in ar if i < p]
    right = [i for i in ar if i > p]
    res = left + [p] + right
    print ' '.join([str(i) for i in res])
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)