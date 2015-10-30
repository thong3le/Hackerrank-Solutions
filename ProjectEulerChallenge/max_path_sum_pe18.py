t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    a = []
    for j in range(n):
        a.append(map(int, raw_input().split()))
    for j in range(n-2,-1,-1):
        for k in range(len(a[j])):
            a[j][k] = max(a[j+1][k]+a[j][k], a[j+1][k+1]+a[j][k])
    print a[0][0]