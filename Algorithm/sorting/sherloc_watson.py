# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k, q = tuple(map(int, raw_input().split()))
a = map(int, raw_input().split())
k %= n
a = a[(n-k):] + a[:(n-k)]
for _ in range(q):
    print a[input()]