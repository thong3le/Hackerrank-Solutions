# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = re.search(r'([A-Za-z0-9])\1', raw_input())
if s:
    print s.group(1)
else:
    print -1