def isSorted(a):
	n = len(a)
	if n <= 1:
		return -1
	for i in range(n-1):
		if a[i+1] < a[i]:
			return i
	return -1

N = input()
a = map(int, raw_input().split())

x = isSorted(a)
if x == -1:
	print "yes"
else:
	j = x
	while j < N-1 and a[j+1] < a[j]:
		j+=1
	b = a[:x] + a[j:(x-1):-1] + a[(j+1):]
	print x, j
	print b
	if isSorted(b) == -1:
		print "reverse {} {}".format(a[j], a[x])
	else: 
		print "no"


