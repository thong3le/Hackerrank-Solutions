# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
a = []
for _ in range(n):
    a.append(input())

candy = [1] * n
for i in range(1, n):
    if a[i-1] < a[i]:
        candy[i] = candy[i-1] + 1
for i in range(n-1, 0, -1):
    if a[i-1] > a[i]:
        candy[i-1] = max(candy[i] + 1, candy[i-1])
        
print sum(candy)