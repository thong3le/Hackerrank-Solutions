from collections import Counter

x = input()
size = Counter(map(int, raw_input().split()))
n = input()
total = 0
for _ in range(n):
    s, p = map(int, raw_input().split())
    if size[s] > 0:
        total += p
        size[s] -= 1
print total