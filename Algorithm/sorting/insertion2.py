#!/bin/python
def insertionSort(ar):    
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]

for i in range(1, m):
    temp = ar[i]
    for j in range(i-1, -1, -1):
        if temp < ar[j]:
            ar[j+1] = ar[j]
            ar[j] = temp
    print ' '.join([str(i) for i in ar])