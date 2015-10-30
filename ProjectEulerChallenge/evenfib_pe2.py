fib = [1,2]
i = 2
while fib[i-1] <= 4*10**16:
    fib.append(fib[i-1]+ fib[i-2])
    i += 1

def evenfib(n):
    s = 0
    for j in range(i):
        if fib[j] <= n and fib[j] % 2 == 0:
            s += fib[j]
    return s

t = int(raw_input())

for k in range(t):
    n = int(raw_input())
    print evenfib(n)