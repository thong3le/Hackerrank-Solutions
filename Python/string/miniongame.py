s = raw_input()
vowels = ['A','E','I','O','U']
kevin = 0;
stuart = 0;

for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
        kevin += len(s) - i
    else:
        stuart +=  len(s) - i
if kevin > stuart:
    print "Kevin %d" % kevin
elif kevin < stuart:
    print "Stuart %d" % stuart
else:
    print "Draw"