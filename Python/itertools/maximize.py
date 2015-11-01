from itertools import product
k, m = map(int, raw_input().split())
N = []
for _ in range(k):
    N.append(map(lambda x:(int(x))**2, raw_input().split()[1:]))
print list(product(*N))
print max([sum(x)%m for x in product(*N)])