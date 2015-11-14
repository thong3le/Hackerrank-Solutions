import math 

s = input()
m = int(math.ceil(math.sqrt(len(s))))
n = int(math.floor(math.sqrt(len(s))))
if m * n < len(s):
    n += 1
encryp = []
for i in range(n):
    encryp.append(s[i*m:(i+1)*m])

last = encryp[-1]
res = []

for i in range(m):
    res.append(''.join([w[i] for w in encryp[:-1]]))

for i in range(len(last)):
    res[i] += last[i]

print ' '.join(res)