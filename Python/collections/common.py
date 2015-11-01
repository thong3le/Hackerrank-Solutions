from collections import Counter

counter = Counter(raw_input())

for i in sorted(counter.items(), key = lambda x: (-x[1], x[0]))[:3]:
    print i[0], i[1]