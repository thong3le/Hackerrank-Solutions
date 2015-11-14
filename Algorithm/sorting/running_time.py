# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
a = map(int, raw_input().split())

shifts = 0

for i in range(1, n):
    j, key = i-1, a[i]
    while j >= 0 and key < a[j]:
        a[j+1] = a[j]
        a[j] = key
        shifts += 1
        j -= 1
print shifts