#!/bin/python

def perfect(H):
    if len(H) == 1:
        return 'Perfect'
    if len(H) % 2 == 0:
        return 'Not perfect'
    for i in range(n//2):
        if H[i+1] <= H[i]:
        return 'Not perfect'
    for i, h in enumerate(reversed(H)):
        if h != H[i]:
            return 'Not perfect'    
    return 'Perfect'

n = int(raw_input().strip())
H = map(int,raw_input().strip().split(' '))
print pefect(H)