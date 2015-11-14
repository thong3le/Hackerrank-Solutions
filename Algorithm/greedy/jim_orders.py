# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
dic = {}
for i in range(1, n+1):
    t, d = map(int, raw_input().split())
    dic[i] = t + d
    
for i, td in sorted(dic.items(), key = lambda x: x[1]):
    print i, 
    