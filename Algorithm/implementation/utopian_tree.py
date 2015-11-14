# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()
for _ in range(tc):
    n = input()
    print 2**((n+1)//2 + 1) - 1 - n%2