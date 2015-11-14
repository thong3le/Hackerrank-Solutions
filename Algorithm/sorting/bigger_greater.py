# Enter your code here. Read input from STDIN. Print output to STDOUT
def nextlexi(s, i):
    head = s[:i]
    c = s[i]
    tail = s[(i+1):]
    j = 0
    while j < len(tail) and tail[j] > c:
        j += 1
    newtail = tail[j-1] + (tail[:j-1] + c + tai[:j])[::-1]

    return head + newtail

tc = input()
for _ in range(tc):
    s = raw_input()
    i = len(s) - 1
    while i > 0 and s[i] <= s[i-1]:
        i -= 1
    if i:
        print nextlexi(s, i-1)
    else:
        print "no answer"