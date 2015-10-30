def largest_product(k, n, num):
	p = 0
	for i in range(n-k+1):
		p = max(p, reduce(lambda x,y: x*y, map(int, num[i:(i+k)])))
	return p

t = int(raw_input())
for _ in range(t):
    s = raw_input().split()
    n = int(s[0])
    k = int(s[1])
    num = raw_input()
    print largest_product(k, n, num)