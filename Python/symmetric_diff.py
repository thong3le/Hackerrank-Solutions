# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
myset1 = set(map(int, raw_input().split()))
M = int(raw_input())
myset2 = set(map(int, raw_input().split()))
myset = myset1 ^ myset2
for i in sorted(myset):
    print i