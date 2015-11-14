# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b,n = tuple(map(int, raw_input().split()))
t = [a,b]
for i in range(2, n):
    t.append(t[i-1]**2 + t[i-2])
    
print t[n-1]