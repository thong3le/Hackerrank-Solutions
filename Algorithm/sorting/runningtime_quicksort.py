# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertionsortshifts(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1], a[j] = a[j], key
            shifts += 1
            j -= 1
    return shifts
        
def quicksort(a, lo, hi):
    if lo < hi:
        p, swaps = partition(a, lo, hi)
        sw1 = quicksort(a, lo, p-1)
        sw2 = quicksort(a, p+1, hi)
        return swaps + sw1 + sw2
    else:
        return 0
def partition(a, lo, hi):
    pivot = a[hi]
    swaps = 0
    i, j = lo, lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            swaps += 1
            i += 1
    a[i], a[hi] = a[hi], a[i]
    swaps += 1
    return i, swaps


n = input()
a = map(int, raw_input().strip().split())
b = [i for i in a]
print insertionsortshifts(b) - quicksort(a, 0, n-1)