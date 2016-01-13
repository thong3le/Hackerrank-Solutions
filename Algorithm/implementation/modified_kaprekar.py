# Enter your code here. Read input from STDIN. Print output to STDOUT

def kaprekar(n):
    d = len(str(n))
    s = str(n**2)
    x = len(s) - d
    if len(s[:x]) != 0:
        return n == int(s[:x]) + int(s[x:])
    else:
        return n == int(s[x:])
    
p = input()
q = input()
flag = True
for n in range(p, q+1):
    if kaprekar(n):
        flag = False
        print n,
if flag:
    print 'INVALID RANGE'