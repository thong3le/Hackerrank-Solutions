import re


fh1 = open('in')
m1 = list()
for line in fh1:
	line = line.rstrip()
	m1.append(line)

fh1.close()

fh2 = open('in2')
m2 = list()
for line in fh2:
	line = line.rstrip()
	m2.append(line)

fh2.close()

m1.sort()
m2.sort()

Regex_Pattern = r'a.[djc]$|abf|[^bd]a$|g$|^d[^di]|^e[^h]|^h(b|e)|^i[^f]|^j[^h]'
print len(Regex_Pattern)
for w in m1:
	if not re.search(Regex_Pattern, w):
		print w

print 

for w in m2:
	if re.search(Regex_Pattern, w):
		print w


def isprime(n):
    return re.search(r'^(hh+?)\1+$', 'h' * n)

print [i for i in range(100) if isprime(i)]