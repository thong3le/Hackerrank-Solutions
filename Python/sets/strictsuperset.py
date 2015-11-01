A = set(raw_input().split())
N = set()
ans = True
for _ in range(input()):
    N = set(raw_input().split())
    ans = ans and len(N-A) == 0 and len(A) > len(N)
print ans