from itertools import product
A = map(int, raw_input().split())
B = map(int, raw_input().split())

for p in product(A, B):
    print p,