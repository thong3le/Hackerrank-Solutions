n = input()
english = set(map(int, raw_input().split()))
n = input()
french = set(map(int, raw_input().split()))

print len(english - french)