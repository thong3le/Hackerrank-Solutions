LIMIT = 41

C = [[0] * 100 for _ in range(101)]
M = [0] * LIMIT

for i in range(LIMIT):
	C[i][0] = 1
	C[i][i] = 1
for i in range(1, LIMIT):
	for j in range(i):
		C[i][j] = C[i-1][j-1] + C[i-1][j]

for i in range(1, LIMIT):
	for j in range(0, i+1, 4):
		M[i] += C[i-j+j//4][j//4]

prime = [False, False, True] + [True, False] * 10**6
for i in range(3, 10**3, 2):
	for j in range(i*i, 10**6, 2*i):
		if prime[j]:
			prime[j] = False

count_primes = [0] * (M[40] + 1)
for i in range(1, len(count_primes)):
	if prime[i]:
		count_primes[i] = count_primes[i-1] + 1
	else:
		count_primes[i] = count_primes[i-1]

def faster_sol(n):
	M1 = [0] * (40+1)
	M1[0] = M1[1] = M1[2] = M1[3] = 1
	for i in range(4, 41):
		M1[i] = M1[i-1] + M1[i-4]
	return count_primes[M1[n]]

tc = input()
for _ in range(tc):
	n = input()
	print faster_sol(n)
