# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
tc = input()
for _ in range(tc):
    n = input()
    a = map(int, raw_input().split())
    dic = Counter(a)
    total = 0
    for k, v in dic.items():
        total += v*(v-1)
    print total