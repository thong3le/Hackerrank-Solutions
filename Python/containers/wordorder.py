from collections import defaultdict

n = int(raw_input())
d = defaultdict(int) 
a = []
for _ in range(n):
    w = raw_input()
    if d[w] == 0:
        a.append(w)
    d[w] += 1
print len(d)
for w in a:
    print d[w],