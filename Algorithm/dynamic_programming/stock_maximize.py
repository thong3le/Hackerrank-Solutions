# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = input()
for _ in range(tc):
    n = input()
    prices = map(int, raw_input().split())
    max_prices = [0]*(n-1) + [prices[-1]]
    for i in range(n-2, -1, -1):
        max_prices[i] = max(max_prices[i+1], prices[i+1])
    profit = 0
    for i in range(n):
        if max_prices[i] - prices[i] > 0:
            profit += max_prices[i] - prices[i]
    print profit  