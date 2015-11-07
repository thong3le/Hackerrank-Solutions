
n = int(raw_input())
a = map(int, raw_input().split())

print "%.3f" % (len(filter(lambda x: x > 0, a)) * 1.0/n)
print "%.3f" % (len(filter(lambda x: x < 0, a))*1.0/n)
print "%.3f" % (len(filter(lambda x: x == 0, a))*1.0/n)