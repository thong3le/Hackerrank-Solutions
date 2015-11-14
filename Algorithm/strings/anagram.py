# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
t = input()
for _ in range(t):
    s = raw_input()
    n = len(s)
    if n%2 != 0:
        print -1
        continue
    dic1 = Counter(s[:n/2])
    dic2 = Counter(s[n/2:])
    d = 0
    for x, c in dic1.items():
        if c - dic2[x] > 0:
            d += c - dic2[x]
    print d