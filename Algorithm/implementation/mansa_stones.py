# Enter your code here. Read input from STDIN. Print output to STDOUT
tc = input()
for _ in range(tc):
    n = input()
    a = input()
    b = input()
    a, b = (min(a,b), max(a,b))
    ret = [(n-1)*a]
    for i in range(1, n):
        tmp = a*(n-1-i) + b*i
        if tmp != ret[-1]:
            ret.append(tmp)
    for i in ret:
        print i,
    print