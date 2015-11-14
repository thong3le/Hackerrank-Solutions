# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
n = input()
ar = [int(i) for i in raw_input().strip().split()]
count = Counter(ar)
print ' '.join([' '.join([str(i)]*count[i]) for i in range(100) if count[i] > 0])