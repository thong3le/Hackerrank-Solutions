from collections import defaultdict, deque

def bfs():
	queue = deque([1])
	visited = set()
	ret = []
	while queue:
		m = len(queue)
		L = set()
		for _ in range(m):
			v = queue.popleft()
			L.add(v)
			visited.add(v)
			queue.extend(tree[v] - visited)
		ret.append(len(L))
	return ret


tc = input()
for _ in range(tc):
	n = input()
	tree = defaultdict(set)
	for _ in range(n-1):
		u,v = map(int, raw_input().strip().split())
		tree[v].add(u)
		tree[u].add(v)
	#print tree
	layers = bfs()
	even = sum([l for i, l in enumerate(layers) if i % 2 == 0])
	odd = sum([l for i, l in enumerate(layers) if i % 2 == 1])
	print even*(even-1)//2 + odd*(odd-1)//2