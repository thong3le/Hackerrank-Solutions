# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

tc = input()
for _ in range(tc):
    a, b = map(int, raw_input().strip().split())
    check = sqrt(a) - int(sqrt(a))
    if check == 0:
        print 1 + int(sqrt(b)) - int(sqrt(a))
    else:
        print int(sqrt(b)) - int(sqrt(a))