# Enter your code here. Read input from STDIN. Print output to STDOUT
def count1bit(A, B):
    if A < 0:
        if B < 0:
            return 32*(B-A+1) - count1bit(-B-1, -A-1)
        else:
            return count1bit(0, B) + count1bit(A, -1)
    
    if A == B:
        return bin(A).count('1')
    if A%2:
        return bin(A).count('1') + count1bit(A+1, B)
    if B%2 == 0:
        return bin(B).count('1') + count1bit(A, B-1)
    return 2*count1bit(A >> 1, B >> 1) + (B+1-A)//2

n = input()
for _ in range(n):
    A, B = map(int, raw_input().split())
    print count1bit(A, B)