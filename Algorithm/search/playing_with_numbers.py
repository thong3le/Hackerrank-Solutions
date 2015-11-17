from bisect import bisect_left, bisect_right

n = input()
a = map(int, raw_input().strip().split())
a.sort()
presum = [abs(a[0])]
for e in a[1:]:
    presum.append(presum[-1] + abs(e))

m = input()
queries = map(int, raw_input().strip().split())

s = 0
for q in queries:
    s += q
    if s >= 0:
        lo = bisect_right(a, -s)
        hi = bisect_left(a , 0)
    else:
        lo = bisect_right(a, 0)
        hi = bisect_left(a, -s)
    
    neg = 0 if lo == 0 else presum[lo-1]
    pos = presum[-1] if hi == 0 else presum[-1] - presum[hi - 1]
    mixed = presum[-1] - neg - pos
    total = (neg - s * lo) + (pos + (n - hi) * s) + abs(mixed - abs((hi - lo) * s))
    
    print total