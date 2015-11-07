
n = input()
result = []
for _ in range(n):
    s = raw_input()
    s = "+91 %s %s" % (s[-10:-5], s[-5:])
    result.append(s)
for e in sorted(result):
    print e
