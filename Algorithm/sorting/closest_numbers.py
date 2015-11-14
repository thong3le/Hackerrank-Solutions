# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
a = map(int, raw_input().strip().split())
a.sort()
min_diff = min([a[i+1] - a[i] for i in range(n-1)])
for i in range(n-1):
    if a[i+1] - a[i] == min_diff:
        print a[i], a[i+1],