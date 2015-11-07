n = input()
res = []
for _ in range(n):
    s = raw_input().split()
    if s[3] == 'F':
        res.append(["Ms. %s %s" % (s[0], s[1]), int(s[2])])
    else:
        res.append(["Mr. %s %s" % (s[0], s[1]), int(s[2])])

for p in sorted(res, key = lambda x: (x[1])):
    print p[0]