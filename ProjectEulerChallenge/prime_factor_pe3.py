def sieve(n):
    prime = [False, False, True] + [True, False] * (n/2)
    for p in range(3, int(n**0.5) + 1, 2):
        if prime[p]:
            for i in range(p*p, n, 2*p):
                prime[i] = False
    return [p for p in range(2,n) if prime[p]]

primes = sieve(10**6)

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    fac = []
    k = 0
    while (n > 1):
        if k >= len(primes):
            fac.append(n)
            break;
        elif n%primes[k] == 0:
            fac.append(primes[k])
            n = n/primes[k]
        else:
            k += 1
    print fac[-1]