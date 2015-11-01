m, n = map(int, raw_input().split())
data = []

for _ in range(m):
    data.append(map(int, raw_input().split()))

k = input()
data = sorted(data, key = lambda x: x[k])
for d in data:
    for e in d:
        print e,
    print