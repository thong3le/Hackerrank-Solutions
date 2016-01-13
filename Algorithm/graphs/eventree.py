# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
def dfs(s):
    stack = [s]
    visited = set()
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(tree[v] - visited)
    return len(visited)

n, m = map(int, raw_input().strip().split())
tree = defaultdict(set)
edges = []
for _ in range(m):
    u, v = map(int, raw_input().strip().split())
    edges.append((u,v))
    tree[u].add(v)
    tree[v].add(u)
    
count = 0
for u, v in edges:
    tree[u].remove(v)
    tree[v].remove(u)
    if dfs(u) % 2 == 0 and dfs(v) % 2 == 0:
        count += 1
    tree[u].add(v)
    tree[v].add(u)
print count