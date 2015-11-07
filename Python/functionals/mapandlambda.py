n = input()
fib = [0,1]
for i in range(2,16):
    fib.append(fib[-1] + fib[-2])
ans = map(lambda x: x**3, fib)

print ans[0:n]