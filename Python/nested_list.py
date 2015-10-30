n = int(raw_input())
marksheet = [[raw_input(), float(raw_input())] for _ in range(n)]
lowest = min(i[1] for i in marksheet)
secondlowest = min(i[1] for i in marksheet if i[1] != lowest)
for i in sorted(name[0] for name in marksheet if name[1] == secondlowest):
    print i