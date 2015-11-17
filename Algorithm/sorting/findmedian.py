from random import randint

def find_kth_smallest(a, lo, hi, k):
    p = partition(a, lo, hi, randint(lo, hi))
    dis = p - lo
    if dis == k:
        return a[p]
    elif k < dis:
        return find_kth_smallest(a, lo, p-1, k) 
    else:
        return find_kth_smallest(a, p+1, hi, k - dis - 1)

def partition(a, lo, hi, index):
    pivot = a[index]
    a[index], a[hi] = a[hi], a[index]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

n = input()
a = map(int, raw_input().strip().split())

print find_kth_smallest(a, 0, n-1, n//2)