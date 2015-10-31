
n = int(raw_input())
w = len(format(n, 'b'))

for i in range(1, n+1):
    print "%s %s %s %s" % (format(i, 'd').rjust(w, " "), format(i, 'o').rjust(w, " "), format(i, 'x').upper().rjust(w, " "), format(i,'b').rjust(w, " "))