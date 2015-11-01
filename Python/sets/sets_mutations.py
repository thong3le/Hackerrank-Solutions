n = input()
a = set(map(int, raw_input().split()))
N = input()

for _ in range(N):
    operation = raw_input().split()
    b = set(map(int, raw_input().split()))
    if operation[0] == "update":
        a |= b
    elif operation[0] == "intersection_update":
        a &= b
    elif operation[0] == "difference_update":
        a -= b
    elif operation[0] == "symmetric_difference_update":
        a ^= b
print sum(a)