# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()
for _ in range(t):
    s1 = set(raw_input())
    s2 = set(raw_input())
    if len(s1 & s2):
        print "YES"
    else:
        print "NO"