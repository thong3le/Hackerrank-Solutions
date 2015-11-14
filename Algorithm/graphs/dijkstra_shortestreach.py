# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq
MAX = float('inf')

tc = input()

for _ in range(tc):
    n, m = map(int, raw_input().split())
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}
    dis = [MAX]*(n+1)
    visited = [False]*(n+1)
    
    for _ in range(m):
        u, v, d = map(int, raw_input().split())
        if v in graph[u] and graph[u][v] <= d:
            continue
        graph[u][v] = d
        graph[v][u] = d
    
    s = input()
    heap = [(0, s)]
    dis[s] = 0

    #print graph

    while heap:
        cost, v = heapq.heappop(heap) 
        if visited[v]:
            continue
        
        visited[v] = True
        for u, d in graph[v].items():
            if not visited[u] and cost + d < dis[u]:
                dis[u] = cost + d
                heapq.heappush(heap, (dis[u], u))
    
    
    for i in range(1, n+1):
        if dis[i] != MAX and dis[i] != 0:
            print dis[i],
        elif dis[i] == MAX:
            print -1,
    print 