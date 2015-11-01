from collections import defaultdict
k = input()
rooms = map(int, raw_input().split())
d = defaultdict(int)
for r in rooms:
    d[r] += 1
for r in set(rooms):
    if d[r] == 1:
        print r