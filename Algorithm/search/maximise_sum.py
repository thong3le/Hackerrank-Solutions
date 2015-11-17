from bisect import insort, bisect_left, bisect_right

tc = input()
for _ in range(tc):
	n, m = map(int, raw_input().strip().split())
	a = map(int, raw_input().strip().split())
	prefix = [0] * n
	total = 0
	for i, e in enumerate(a):
		total += e
		prefix[i] = total % m

	bst = []
	max_sum = 0
	for s in prefix:
		i = bisect_right(bst, s)
		max_sum = max(max_sum, s) if i >= len(bst) else max(max_sum, (s-bst[i]+m) % m)
		insort(bst, s)
	print max_sum
