
def sum_multiples(b, n):
    t = n/b
    return b*t*(t+1)/2

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print sum_multiples(3, n-1) + sum_multiples(5, n-1) - sum_multiples(15, n-1)