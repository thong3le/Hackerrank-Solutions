from collections import defaultdict 

d = defaultdict(list)
n, m = map(int, raw_input().split())

for i in range(1, n+1):
	d[raw_input()].append(i)

for i in range(m):
	a = d[raw_input()]
	if (len(a) > 0):
		for e in a:
			print e,
		print 
	else:
		print -1