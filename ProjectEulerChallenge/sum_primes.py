primes = [False, False, True] + [True, False] * (10**6/2)

for p in range(3, 10**3+1, 2):
    if primes[p]:
        for i in range(p*p, 10**6+1, 2*p):
            primes[i] = False
        
sum_primes = [0];

for i in range(1, 10**6+1):
    if primes[i]:
        sum_primes.append(sum_primes[i-1] + i)
    else:
        sum_primes.append(sum_primes[i-1])

t = int(raw_input())
for i in range(t):
    print sum_primes[int(raw_input())]