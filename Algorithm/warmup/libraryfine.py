d1, m1, y1 = map(int, raw_input().split())
d2, m2, y2 = map(int, raw_input().split())

if y1 > y2:
    print 10000
elif y1 < y2:
    print 0
elif m1 > m2:
    print (m1-m2)*500
elif m1 < m2:
    print 0
elif d1 >= d2:
    print (d1-d2)*15
elif d1 < d2:
    print 0
