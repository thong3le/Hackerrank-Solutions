import re

n = input()
ptrn1 = re.compile(r'(?<= )&&(?= )')
ptrn2 = re.compile(r'(?<= )\|\|(?= )')
for _ in range(n):
    s = raw_input()
    s = re.sub(ptrn1, "and", s)
    s = re.sub(ptrn2, "or", s)
    print s