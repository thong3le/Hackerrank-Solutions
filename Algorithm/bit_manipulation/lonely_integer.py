#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    for e in a:
        answer ^= e
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)