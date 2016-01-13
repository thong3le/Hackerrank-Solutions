from collections import defaultdict, deque
import heapq

def bridges():
	for v in graph.keys():
		if pre[v] == -1:
			dfs(v, v)

def dfs(u, v):
	global cnt
	pre[v] = cnt
	cnt += 1
	low[v] = pre[v]

	for w in graph[v].keys():
		if pre[w] == -1:
			dfs(v, w)
			low[v] = min(low[v], low[w])
			if low[w] == pre[w]:
				cut_edges.append((v,w))
				graph[v][w] = 1
				graph[w][v] = 1
		elif w != u:
			low[v] = min(low[v], pre[w])

def dfs2(s):
	stack = [s]
	visited = set()
	while stack:
		v = stack.pop()
		if v not in visited:
			visited.add(v)
			for w in graph[v].keys():
				if graph[v][w] == 0:
					stack.append(w)
	return visited

def bfs(s, tree, p):
	queue = deque([s])
	ret = len(s)
	for _ in range(p):
		m = len(queue)
		for _ in range(m):
			v = queue.popleft()
			for u in tree[v]:
				ret += len(u)
				queue.append(u)
	return ret

def cc(p):
	ret = [0] * (n+1)
	tree = defaultdict(set)
	vtoi = {}
	itov = {}
	for u, v in cut_edges:
		c1 = tuple(dfs2(u))
		c2 = tuple(dfs2(v))
		
		tree[c1].add(c2)
		tree[c2].add(c1)
	for v in tree.keys():
		x = bfs(v, tree, p)
		for i in v:
			ret[i] = x - 1 
	return ret



n, e, p = map(int, raw_input().strip().split())
graph = defaultdict(dict)
for _ in range(e):
	u, v = map(int, raw_input().strip().split())
	graph[u][v] = 0
	graph[v][u] = 0

cnt = 0	
cut_edges = []
low = [-1] * (len(graph)+1)
pre = [-1] * (len(graph)+1)

bridges()

res = cc(p)

for i in range(1, n+1):
	print res[i]

