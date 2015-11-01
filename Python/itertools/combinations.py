from itertools import combinations

a,b = raw_input().split()

for i in range(1, int(b)+1):
    for c in combinations(sorted(a), i):
        print "".join(c)