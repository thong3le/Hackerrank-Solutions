# Enter your code here. Read input from STDIN. Print output to STDOUT
def AND(A, B):
    if A == 0 or B == 0 or len(bin(A)) != len(bin(B)):
        return 0
    p = 2**int(len(bin(A)) - 3)
    return p + AND(A%p, B%p)
    
tc = input()

for _ in range(tc):
    A, B = map(int, raw_input().split())
    print AND(A, B)