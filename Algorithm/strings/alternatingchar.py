n = input()
for _ in range(n):
    s = raw_input()
    res = [s[0]]
    d = 0
    for i in range(1, len(s)):
        if s[i] != res[-1]:
            res.append(s[i])
        else:
            d += 1
    print d
