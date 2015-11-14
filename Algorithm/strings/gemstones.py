# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
gem = set(raw_input())
for _ in range(n-1):
    gem &= set(raw_input()) 
print len(gem)