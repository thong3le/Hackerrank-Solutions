n = int(raw_input())
a = []
for _ in range(n):
    a.append(map(int, raw_input().split()))
    
d1 = 0
d2 = 0

for i in range(n):
    d1 += a[i][i]
    d2 += a[n-1-i][i]

print max(d1-d2, d2-d1)