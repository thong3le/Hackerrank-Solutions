def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		v, path = stack.pop()
		for next in graph[v] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))

graph = {
	1: set([2, 3, 4]),
	2: set([1, 3, 4]),
	3: set([1, 2, 4]),
	4: set([1, 2, 3])
}

for i in dfs_paths(graph, 1, 4):
	print i