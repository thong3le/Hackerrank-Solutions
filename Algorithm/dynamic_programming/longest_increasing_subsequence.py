from bisect import bisect_left
def lis1(d):
	lis = []
	for i in range(len(d)):
		lis.append(max([lis[j] for j in range(i) if lis[j][-1] < d[i]] or [[]], key = len) + [d[i]])
	return max(lis, key = len)

def lis2(d):
	n = len(d)
	p = [0] * n
	m = [0] * (n+1)
	L = 0
	for i in range(n):
		lo = 1
		hi = L
		while lo <= hi:
			mid = (lo + hi)//2
			if (d[m[mid]] < d[i]):
				lo = mid + 1
			else:
				hi = mid - 1
		newL = lo
		p[i] = m[newL-1]
		m[newL] = i

		if (newL > L):
			L = newL

	lis = []
	k = m[L]
	for i in range(L-1, -1, -1):
		lis.append(d[k])
		k = p[k]
	
	print p
	print m

	return lis[::-1]

def lis3(d):
	piles, top_piles = [], []
	for i in range(len(d)):
		j = bisect_left(top_piles, d[i])
		if j < len(top_piles):
			piles[j].append(d[i])
			top_piles[j] = d[i]
		else:
			piles.append([d[i]])
			top_piles.append(d[i])
	return top_piles

n = input()
a = []
for _ in range(n):
    a.append(input())

print lis3(a)