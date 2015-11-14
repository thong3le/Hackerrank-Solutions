# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
a = map(int, raw_input().split())
p, q = map(int, raw_input().split())

dic = {}
dic[p] = min([abs(x-p) for x in a])
dic[q] = min([abs(x-q) for x in a])
a.sort()
for i in range(n-1):
    mid = (a[i] + a[i+1])//2
    if mid > p and mid < q and mid - a[i]:
        dic[mid] = mid - a[i]

print sorted(dic.items(), key = lambda x: (-x[1], x[0]))[0][0]