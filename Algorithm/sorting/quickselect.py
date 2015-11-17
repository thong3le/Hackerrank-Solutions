import random
 
def partition(vector, lo, hi, pivotIndex):
    pivot = vector[pivotIndex]
    vector[pivotIndex], vector[hi] = vector[hi], vector[pivotIndex]  # Move pivot to end
    p = lo
    for i in range(lo, hi):
        if vector[i] < pivot:
            vector[p], vector[i] = vector[i], vector[p]
            p += 1
    vector[hi], vector[p] = vector[p], vector[hi]  # Move pivot to its final place
    return p
 
def _select(vector, lo, hi, k):
    "Returns the k-th smallest, (k >= 0), element of vector within vector[lo:hi+1] inclusive."
    p = partition(vector, lo, hi, random.randint(lo, hi))
    dis = p - lo
    if dis == k:
        return vector[p]
    elif k < dis:
        return _select(vector, lo, p - 1, k)
    else:
        return _select(vector, p+1, hi, k - dis - 1)
 
def select(vector, k, lo=None, hi=None):
    """\
    Returns the k-th smallest, (k >= 0), element of vector within vector[lo:hi+1].
    lo, hi default to (0, len(vector) - 1) if omitted
    """
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(vector) - 1
    assert vector and k >= 0, "Either null vector or k < 0 "
    assert 0 <= lo <= len(vector) - 1, "lo is out of range"
    assert lo <= hi <= len(vector) - 1, "hi is out of range"
    return _select(vector, lo, hi, k)
 
if __name__ == '__main__':
    v = [3, 4, 2, 3, 2, 3, 2, 1, 3, 2]
    print([select(v, i) for i in range(10)])