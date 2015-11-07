import re

n = input()
result = []
for _ in range(n):
    result.append(raw_input())
    
ptrn = re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$") 
print sorted(filter(lambda x: re.search(ptrn, x), result))