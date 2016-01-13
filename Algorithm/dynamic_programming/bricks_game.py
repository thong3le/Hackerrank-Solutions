def optimal(a):
	pre_sum = 0
	n = len(a)
	ret = [0] * (n + 3)
	pre_sum = 0
	for i in range(n-1, -1, -1):
		pre_sum += a[i] 
		ret[i] = pre_sum - min(ret[i+1], ret[i+2], ret[i+3])
	return ret[0]

def bottom_up(a):
	n = len(a)

	a.append(0)
	a.reverse()
	
	dp = [0] * (n+1)
	pre_sum = [0] * (n+1)
	
	for i in range(1, n+1):
		pre_sum[i] = pre_sum[i-1] + a[i]

	dp[0] = 0
	dp[1] = pre_sum[1]
	dp[2] = pre_sum[2] 
	dp[3] = pre_sum[3]

	for i in range(4, n+1):
		opt1 = pre_sum[i-1] - dp[i-1] + a[i]
		opt2 = pre_sum[i-2] - dp[i-2] + a[i] + a[i-1]
		opt3 = pre_sum[i-3] - dp[i-3] + a[i] + a[i-1] + a[i-2]
		dp[i] = max(opt1, opt2, opt3)

	return dp[n]

#default maximum depth is 999
def topdown(a, pre_sum):
	n = len(a)
	if n <= 3:
		OPT[n] = pre_sum[-1]
		return OPT[n]
	if OPT[n] != -1:
		return OPT[n]
	else:
		opt1 = pre_sum[-2] - topdown(a[:-1], pre_sum[:-1]) + a[-1]
		opt2 = pre_sum[-3] - topdown(a[:-2], pre_sum[:-2]) + a[-1] + a[-2]
		opt3 = pre_sum[-4] - topdown(a[:-3], pre_sum[:-3]) + a[-1] + a[-2] + a[-3]
		OPT[n] = max(opt1, opt2, opt3)
		return OPT[n]


tc = input()
for _ in range(tc):
	n = input()
	a = map(int, raw_input().split())
	a.reverse()
	pre_sum = [0] * n
	OPT = [-1] * (10**5 + 1)
	pre_sum[0] = a[0]
	for i in range(1, n):
		pre_sum[i] = pre_sum[i-1] + a[i]
	print topdown(a, pre_sum)