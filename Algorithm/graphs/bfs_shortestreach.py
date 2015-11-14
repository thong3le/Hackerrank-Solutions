from collections import deque
tc = input()

for _ in range(tc):
    n, m = map(int, raw_input().split())
    graph = {}
    for i in range(1, n+1):
        graph[i] = set()
    for _ in range(m):
        u, v = map(int, raw_input().split())
        graph[u].add(v)
        graph[v].add(u)

    s = input()
    dis = [-1] * (n+1)
    visited = [False] * (n+1) 
    queue = deque([s])
    
    dis[s] = 0
    visited[s] = True

    while queue:    
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)
                dis[u] = dis[v] + 6
           
    for i in range(1, n+1):
        if dis[i]:
            print dis[i],
    print 
