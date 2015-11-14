# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()
for _ in range(tc):
    s1 = raw_input()
    s2 = raw_input()
    i, j = 0, 0
    s1 += 'z'
    s2 += 'z'
    res = ''
    while i < len(s1) and j < len(s2):
        if s1[i:] < s2[j:]:
            res += s1[i]
            i += 1
        else:
            res += s2[j]
            j += 1
            
    while i < len(s1):
        res += s1[i]
        i += 1
    while j < len(s2):
        res += s2[j]
        j += 1
    print res[:-2]