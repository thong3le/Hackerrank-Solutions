# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().strip().split())
a = map(int, raw_input().strip().split())
b = map(int, raw_input().strip().split())

dp = [[0]*(m+1) for _ in range(n+1)]
for i, x in enumerate(a):
    for j, y in enumerate(b):
        dp[i+1][j+1] = 1 + dp[i][j] if x ==y else max(dp[i+1][j], dp[i][j+1])

opt = []
i, j = n, m
while i != 0 and j != 0:
	if dp[i][j] == dp[i][j-1]:
		j -= 1
	elif dp[i][j] == dp[i-1][j]:
		i -= 1
	else:
		opt.append(a[i-1])
		i -= 1
		j -= 1

print ' '.join([str(i) for i in opt[::-1]])