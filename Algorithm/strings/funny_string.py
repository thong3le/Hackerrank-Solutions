# Enter your code here. Read input from STDIN. Print output to STDOUT
t = input()
for _ in range(t):
    s = raw_input()
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            print "Not Funny"
            break
    else:
        print "Funny"