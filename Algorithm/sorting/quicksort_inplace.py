# Enter your code here. Read input from STDIN. Print output to STDOUT
def quicksort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)
def partition(a, lo, hi):
    pivot = a[hi]
    i, j = lo, lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    print ' '.join([str(e) for e in a])
    return i


n = input()
a = map(int, raw_input().strip().split())
quicksort(a, 0, n-1)