n = input()
a = map(int, raw_input().split())

while a:
    m = min(a)
    a = map(lambda x: x - m, a)
    print len(a)
    a = filter(lambda x: x, a)