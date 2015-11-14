tc = input()
for _ in range(tc):
    n = input()
    c3 = 5*(2*n%3)
    if c3 <= n:
        print '5' * (n - c3) + '3' * c3
    else: 
        print -1