# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = input()
ar = [int(i) for i in raw_input().strip().split()]
count = Counter(ar)
print ' '.join([str(count[i]) for i in range(100)])