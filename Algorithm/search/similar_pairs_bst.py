from bisect import insort, bisect_left, bisect_right

def search(parent, children, root, T, N):
    node = root
    total = 0
    stack = [node]
    values = [node]
    while node:
        if children[node]:
            c = node = children[node].pop()
            m, x = c - T, c + T
            im = bisect_left(values, m)
            ix = bisect_right(values, x)
            total += ix - im
            insort(values, c)
            stack.append(c)
        else:
            values.pop(bisect_left(values, stack.pop()))
            node = parent[node]
    return total
        

n, T = map(int, raw_input().strip().split())
children = [[] for i in xrange(n + 1)]
parent = [None] * (n + 1)
root = 0
for i in range(n-1):
    si, ei = map(int, raw_input().strip().split())
    children[si].append(ei)
    parent[ei] = si
    if root == 0 or ei == root:
        root = si

print search(parent, children, root, T, n)