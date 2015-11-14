tctc = input()
for _ in range(tc):
    R, C = map(int, raw_input().split())
    digits = []
    for _ in range(R):
        digits.append(raw_input())
    r, c = map(int, raw_input().split())
    ptn = ''
    for _ in range(r):
        ptn += raw_input()
    flag = False
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            if digits[i][j:(j+c)] == ptn[0:c]:
                s = ''
                for k in range(i, i + r):
                    s += digits[k][j:(j+c)]
                if s == ptn:
                    print "YES"
                    flag = True
                    break
        if flag: 
            break
    if not flag:
        print "NO"