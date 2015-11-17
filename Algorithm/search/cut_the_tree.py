# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n = input()
w = map(int, raw_input().strip().split())
tree = defaultdict(set)
sum_node = [0] * n
for _ in range(n-1):
    u, v = map(int, raw_input().strip().split())
    tree[u].add(v)
    tree[v].add(u)

visited, stack = set(), [1]
ordering = []
children = defaultdict(set)
while stack:
    v = stack.pop()
    visited.add(v)
    ordering.append(v)
    children[v] = tree[v] - visited
    stack.extend(children[v])

for v in reversed(ordering):
    sum_node[v-1] = w[v-1] + sum([sum_node[c-1] for c in children[v]])

total = sum(w)

print min(abs(total - 2*s) for s in sum_node[1:])