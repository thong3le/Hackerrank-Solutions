# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()

for _ in range(tc):
    B, W = map(int, raw_input().split())
    X, Y, Z = map(int, raw_input().split())
    
    if X + Z < Y:
        print B*X + W*(X+Z)
    elif Y + Z < X:
        print B*(Y+Z) + W * Y
    else:
        print B*X + W*Y