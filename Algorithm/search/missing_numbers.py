# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = input()
a = Counter(map(int, raw_input().split()))
m = input()
b = Counter(map(int, raw_input().split()))

res = []
for x, c in b.items():
    if c - a[x] > 0:
        res.append(x)

res.sort()
for x in res:
    print x,