N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
min_diff = lists[-1]
for i in range(N-K+1):
    min_diff = min(min_diff, lists[i+K-1] - lists[i])

print min_diff