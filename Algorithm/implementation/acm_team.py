from itertools import combinations

n, m = map(int, raw_input().split())

data = []
for _ in range(n):
	data.append(int(raw_input(), 2))

res = [bin(a | b).count('1') for a, b in combinations(data, 2)]

maximal = max(res)

print maximal
print res.count(maximal)