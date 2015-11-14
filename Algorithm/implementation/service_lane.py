n, tc = map(int, raw_input().split())
width = map(int, raw_input().split())

for _ in range(tc):
    i, j = map(int, raw_input().split())
    print min(width[i:(j+1)])