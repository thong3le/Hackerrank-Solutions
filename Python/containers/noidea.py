from collections import defaultdict

m,n = map(int, raw_input().split())
d = defaultdict(int)
array = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
for e in A:
    d[e] = 1
for e in B:
    d[e] = -1
score = 0;

for e in array:
    score += d[e]
    
print score