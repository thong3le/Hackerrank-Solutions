# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    n = A/B; total = n + n/C1
    m = n/C1 + n%C1  
    while m >= C1:
        total += m/C1
        m = m/C1 + m%C1
    
    print total

