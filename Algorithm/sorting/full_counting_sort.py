# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n = input()
ar = []
for _ in range(n//2):
    s = raw_input().strip().split()
    ar.append((int(s[0]), '-'))
for _ in range(n//2):
    s = raw_input().strip().split()
    ar.append((int(s[0]), s[1]))
dic = defaultdict(list)
for i, s in ar:
    dic[i].append(s)
for i in range(100):
    print ' '.join(dic[i]),