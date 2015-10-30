# Enter your code here. Read input from STDIN. Print output to STDOUT
prime = [2,3,5,7,11,13,17,19,23,29,31,37]
def factors(n):
    fac = [0]*12
    i = 0
    while n > 1:
        if n%prime[i] == 0:
            fac[i] += 1
            n /= prime[i]
        else:
            i += 1
    return fac
	

def smallest_multiple(n):
	if n <= 1:
		return 1
	fac = [0]*12
	for i in range(1, n+1):
		fac = map(lambda x,y: max(x,y), fac, factors(i))
	
	s = 1
	for i in range(len(prime)):
		s *= prime[i] ** fac[i]
	return s

t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	print smallest_multiple(n)



