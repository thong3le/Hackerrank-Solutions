# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()

for _ in range(tc):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    
    a.sort()
    b.sort()
    
    for i in range(n):
        if a[i] + b[n-1-i] < k:
            print "NO"
            break
    else:
        print "YES"