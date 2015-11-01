m, n = map(int, raw_input().split())
score = []
for _ in range(n):
    score.append(map(float, raw_input().split()))

for e in zip(*score):
    print sum(e)/n