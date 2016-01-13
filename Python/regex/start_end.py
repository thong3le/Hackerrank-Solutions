# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = raw_input()
w = raw_input()
m = re.finditer(r'(?=(%s))' % w, s)
flag = False
for g in m:
    flag = True
    print (g.start(), g.end() + len(w) - 1)

if not flag:
    print (-1,-1)