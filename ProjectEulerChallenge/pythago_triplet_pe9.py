def pythago(n):
    triple = []
    for c in range(n/3, n-3):
        s = n - c
        p = (n**2 - 2*n*c)/2.0
        delta = s**2 - 4*p
        if delta >= 0 and p > 0:
            if int(delta**0.5) - delta**0.5 == 0:
                a = (s - delta**0.5)/2.0
                b = (s + delta**0.5)/2.0
                triple.append((int(a),int(b),c))
    
    return triple

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    p = map(lambda x: x[0]*x[1]*x[2], pythago(n))
    if len(p) == 0:
        print -1
    else:
        print max(p) 