# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()
for _ in range(tc):
    n, k = map(int, raw_input().strip().split())
    a = map(int, raw_input().strip().split())
    dp = [0] * (k+1)
    for i in range(n):
        for j in range(1, k+1):
            if j >= a[i]:
                dp[j] = max(dp[j], dp[j-a[i]] + a[i])
    print dp[-1]