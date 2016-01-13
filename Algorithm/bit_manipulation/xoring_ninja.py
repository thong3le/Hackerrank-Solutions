tc = input()
for _ in range(tc):
    n = input()
    print 2**(n-1)*reduce(lambda x, y: x | y, map(int, raw_input().split())) % (10**9+7)