def dfs_path(forest, start, goal):
	n = len(forest)
	m = len(forest[0])
	stack = [(start, [start])]
	while stack:
		v, path = stack.pop()
		i, j = v
		for next in find_neighbors(forest, i, j) - set(path):
			if next == goal:
				return path + [next]
			else:
				stack.append((next, path + [next]))

def find_neighbors(forest, i, j):
	neighbor = set([])
	if i < n-1 and (forest[i+1][j] == '.' or forest[i+1][j] == '*'):
		neighbor.add((i+1, j))
	if j < m-1 and (forest[i][j+1] == '.' or forest[i][j+1] == '*'):
		neighbor.add((i, j+1))
	if i > 0 and (forest[i-1][j] == '.' or forest[i-1][j] == '*'):
		neighbor.add((i-1, j))
	if j > 0 and (forest[i][j-1] == '.' or forest[i][j-1] == '*'):
		neighbor.add((i, j-1))
	return neighbor

tc = input()
for _ in range(tc):
	n, m = map(int, raw_input().strip().split())
	forest = []
	for _ in range(n):
		forest.append(raw_input())
	k = input()

	for i in range(n):
		for j in range(m):
			if forest[i][j] == 'M':
				start = (i,j)
			if forest[i][j] == '*':
				goal = (i,j)

	path = dfs_path(forest, start, goal)
	count = 0 
	for i in range(len(path) - 1):
		v1, v2 = path[i]
		if len(find_neighbors(forest, v1, v2) - set(path[:i])) > 1:
			count += 1

	if count == k:
		print "Impressed"
	else: 
		print "Oops!"
