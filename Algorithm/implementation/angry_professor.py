# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()
for _ in range(tc):
    n, k = map(int, raw_input().split())
    arrives = map(int, raw_input().split())
    if len(filter(lambda x: x <= 0, arrives)) >= k:
        print "NO"
    else:
        print "YES"
