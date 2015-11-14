# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
ar = []
for _ in range(n):
    s = raw_input().strip().split()
    ar.append(int(s[0]))
count = [0]*100
totalcount = [0]*100
for i in ar:
    count[i] += 1
totalcount[0] = count[0]
for i in range(100):
    totalcount[i] = totalcount[i-1] + count[i] 

print ' '.join([str(i) for i in totalcount])