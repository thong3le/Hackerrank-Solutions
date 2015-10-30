
def sieve(n):
	prime = [False, False, True] + [True, False] * (n/2)
	for p in range(3, int(n**0.5) + 1, 2):
		for j in range(p*p, n+1, 2*p):
			prime[j] = False
	return [p for p in range(n+1) if prime[p]]

primes = sieve(10**6)

def factors(n):
	fac = 1
	for i in primes:
		if (i * i > n):
			return fac * 2
		exp = 1
		while (n % i == 0):
			exp += 1
			n = n / i
		fac *= exp

		if (n == 1):
			return fac
	return fac

def n_divisors(n):
	number = 1
	i = 2;
	while (factors(number) < n+1):
		number += i
		i += 1
	return number

n = int(raw_input())
for _ in range(n):
	print n_divisors(int(raw_input()))