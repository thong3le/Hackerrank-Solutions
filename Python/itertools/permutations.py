from itertools import permutations

a,b = raw_input().split()

for p in permutations(sorted(a), int(b)):
    print "".join(p)