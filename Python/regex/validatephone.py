import re
p = re.compile('[789][0-9]{9}')
n = input()
for _ in range(n):
    s = raw_input()
    if re.match(p, s) and len(s) == 10:
        print "YES"
    else:
        print "NO"