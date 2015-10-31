s = raw_input()
a, b = tuple(raw_input().split())
l = list(s)
l[int(a)] = b

print "".join(l)