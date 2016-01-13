MOD = 1000000007
LIMIT = 300
C = [[0]*(LIMIT+1) for _ in range(LIMIT+1)]

def combination():
	for i in range(LIMIT + 1):
		C[i][0] = 1
		C[i][i] = 1
	for i in range(1, LIMIT+1):
		for j in range(1, i):
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

def grid_walking(X, D, M):
	N = len(X)
	dpx = [[0]*(N+1) for _ in range(M+1)]
	for i in range(N):
		d = D[i]
		dpxi = [[0]*(M+1) for _ in range(d+1)]

		for j in range(1, d+1):
			dpxi[j][0] = 1

		for k in range(1, M+1):
			for j in range(1, d+1):
				if  j > 1:
					dpxi[j][k] = (dpxi[j][k] + dpxi[j-1][k-1]) % MOD
				if j + 1 <= d:
					dpxi[j][k] = (dpxi[j][k] + dpxi[j+1][k-1]) % MOD
		
		dpx[0][i+1] = 1

		for j in range(1, M+1):
			dpx[j][i+1] = dpxi[X[i]][j]


	dp = [[0] * (N+1) for _ in range(M+1)]

	for i in range(M+1):
		dp[i][1] = dpx[i][1]
	for i in range(N+1):
		dp[0][i] = 1;

	for i in range(2, N+1):
		for j in range(1, M+1):
			for k in range(0, j+1):
				dp[j][i] = (dp[j][i] + (C[j][j-k] * dp[k][i-1] * dpx[j-k][i]) % MOD) % MOD


	return dp[M][N]

tc = input()
for _ in range(tc):
	N, M = map(int, raw_input().split())
	X = map(int, raw_input().split())
	D = map(int, raw_input().split())
	
	combination();

	print grid_walking(X, D, M)