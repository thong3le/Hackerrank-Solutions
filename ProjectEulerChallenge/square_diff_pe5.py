def square_diff(n):
    s1 = (n*(n+1)/2)**2
    s2 = n*(n+1)*(2*n+1)/6
    return s1 - s2

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print square_diff(n) 