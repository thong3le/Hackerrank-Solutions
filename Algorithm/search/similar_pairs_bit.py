class Bit:
	def __init__(self, n):
		self.data = [0] * (n+1)
		self.size = n

	def add (self, index, val = 1):
		while index <= self.size:
			self.data[index] += val
			index += index & -index

	def get(self, index):
		ret = 0
		while index > 0:
			ret += self.data[index]
			index -= index & -index
		return ret


def dfs(s, bit):
	ret = 0
	stack = [s]
	bit.add(s)
	next = [0] * (n+1)
	while stack:
		v = stack[-1]
		i = next[v]
		if i < len(tree[v]):
			child = tree[v][idx]
			ret += bit.get(min(child + t, n)) - bit.get(child - t -1)
			stack.append(child)
			bit.add(child)
			next[v] += 1
		else:
			stack.pop()
			bit.add(v, -1)
	return ret

n, t = map(int, raw_input().strip().split())
tree = [[] for x in range(n+1)]
isroot = [True] * (n+1)
for x in range(n-1):
	a, b = map(int, raw_input().strip().split())
	tree[a].append(b)
	isroot[b] = False

for x in range(1, n+1):
	if isroot[x]:
		print dfs(x, Bit(n))
		break
