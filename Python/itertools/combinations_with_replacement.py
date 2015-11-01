from itertools import combinations_with_replacement

a,b = raw_input().split()

for c in combinations_with_replacement(sorted(a), int(b)):
    print "".join(c)