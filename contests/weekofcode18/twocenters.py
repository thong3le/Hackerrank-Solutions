from collections import defaultdict, deque

def path(s, f, graph):
	dis = [-1] * (N+1)
	dis[s] = 0
	queue = deque([s])
	while queue:
		v = queue.popleft()
		for u in graph[v]:
			if dis[u] == -1 and u != f:
				queue.append(u)
				dis[u] = dis[v] + 1
	return dis


def bfs(s, graph):
	dis = [-1] * (N+1)
	dis[s] = 1
	queue = deque([s])
	while queue:
		v = queue.popleft()
		for u in graph[v]:
			if dis[u] == -1:
				queue.append(u)
				dis[u] = dis[v] + 1
	return max(dis)

def neighbor_dis(s):
	graph = defaultdict(set)
	for v in tree.keys():
		graph[v] = tree[v].copy()

	graph.pop(s)
	for u in tree[s]:
		graph[u].remove(s)

	neighbor = {}
	for u in tree[s]:
		neighbor[u] = bfs(u, graph)
	return neighbor 

def find():
	ret = float('inf')
	for s in range(1, N+1):
		d = neighbor_dis(s)

		v1, x1 = max(d.items(), key = lambda x: x[1])
	
		if len(d) <= 1:
			ret = min(ret, x1//2)
			continue

		d.pop(v1)
		v2, x2 = max(d.items(), key = lambda x: x[1])
		ret = min(ret, max(x1//2, x2))

	print ret


N = input()
tree = defaultdict(set)

for _ in range(N-1):
	u, v = map(int, raw_input().split())
	tree[u].add(v)
	tree[v].add(u)
#print tree


ret = float('inf')

for s in range(1, N):
	for f in range(s+1, N+1):
		d1 = path(s, f, tree)
        d2 = path(f, s, tree)
        print s, f, d1, d2
        d = []
        for i in range(1, N+1):
            if d1[i] == -1:
                d.append(d2[i])
            elif d2[i] == -1:
                d.append(d1[i])
            else:
                d.append(min(d1[i], d2[i]))
		ret = min(ret, max(d))
print ret