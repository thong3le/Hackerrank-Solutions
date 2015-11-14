#!/usr/bin/py
# Head ends here
from itertools import combinations

def pairs(a,k):
    dic = {}
    answer = 0
    for i in a:
        dic[i] = 1
    for i in a:
        if (i+k) in dic:
            answer += 1
    return answer

def pairs2(a,k):
    if len(a) <= 1:
        return 0
    answer = [abs(x-y) for x,y in combinations(a, 2)].count(k)
    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)