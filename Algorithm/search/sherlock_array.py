# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()
for _ in range(tc):
    n = input()
    a = map(int, raw_input().split())
    total = sum(a)
    right = total
    for i in range(n):
        right -= a[i]
        left = total - a[i] - right
        if left == right:
            print "YES"
            break
    else:
        print "NO"