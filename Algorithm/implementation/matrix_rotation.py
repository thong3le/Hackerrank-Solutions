def rotate(A, m, n, r):
	k = min(m, n) // 2
	parts = []
	for i in range(k):
		tmp = []
		for j in range(i, m - i):
			tmp.append(A[j][i])
		for j in range(i+1, n - i):
			tmp.append(A[m-1-i][j])
		for j in range(m-1-i-1, i-1, -1):
			tmp.append(A[j][n-i-1])
		for j in range(n-1-i-1, i, -1):
			tmp.append(A[i][j])
		parts.append(tmp)
	for i in range(k):
		x = len(parts[i]) - r % len(parts[i])
		tmp = parts[i][x:] + parts[i][:x] 
		index = 0
		for j in range(i, m - i):
			A[j][i] = tmp[index]
			index += 1
		for j in range(i+1, n - i):
			A[m-1-i][j] = tmp[index]
			index += 1
		for j in range(m-1-i-1, i-1, -1):
			A[j][n-i-1] = tmp[index]
			index += 1
		for j in range(n-1-i-1, i, -1):
			A[i][j] = tmp[index]
			index += 1
	for i in range(m):
		for j in range(n):
			print A[i][j],
		print

m, n, r = map(int, raw_input().strip().split())
A = []
for _ in range(m):
	A.append(map(int, raw_input().strip().split()))
rotate(A, m, n, r)