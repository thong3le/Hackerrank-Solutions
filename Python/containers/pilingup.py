from collections import deque

tc = int(raw_input())

for _ in range(tc):
    n = int(raw_input())
    sides = deque(map(int, raw_input().split()))
    base = 2**31
    flag = True
    while len(sides) > 0:
        if max(sides[0], sides[-1]) > base:
            print "No"
            flag = False
            break
        elif sides[0] >= sides[-1]:
            base = sides.popleft()
        else:
            base = sides.pop()
    if flag:
        print "Yes"