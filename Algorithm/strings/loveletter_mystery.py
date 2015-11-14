# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()
for _ in range(t):
    s = raw_input()
    d = 0
    for i in range(len(s)//2):
        d += abs(ord(s[i]) - ord(s[-(i+1)]))
    print d