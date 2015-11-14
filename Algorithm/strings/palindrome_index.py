# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()
for _ in range(t):
    s = raw_input()
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            p = s[:i] + s[(i+1):]
            if p == p[::-1]:
                print i
                break
            x = len(s) - i - 1
            p = s[:x] + s[(x+1):]
            if p == p[::-1]:
                print x
                break
    else:
        print -1