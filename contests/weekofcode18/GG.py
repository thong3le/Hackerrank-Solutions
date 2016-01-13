from itertools import permutations

s = raw_input()
n = len(s) + 1
a = range(n)
count = 0
for p in permutations(a):
	flag = False
	for i in range(len(s)):
		if s[i] == 'G' and p[i] <= p[i+1]:
			flag = not flag
			break
		elif s[i] == 'L' and p[i] >= p[i+1]:
			flag = not flag
			break
	if not flag:
		count += 1
		print p
print count