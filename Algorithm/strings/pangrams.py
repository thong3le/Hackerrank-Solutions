# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input()

pangram = set([ord(c.lower()) for c in s if c.isalpha()])

if pangram == set(range(ord('a'), ord('z') + 1)):
    print "pangram"
else:
    print "not pangram"