
def sieve(n):
    prime = [False, False, True]+[True, False]*(n/2)
    for p in range(3, int(n**0.5) + 1, 2):
        for i in range(p*p, n, 2*p):
            prime[i] = False
    return [p for p in range(1, n+1) if prime[p]]

primes = sieve(2 * 10**5)


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print primes[n-1]