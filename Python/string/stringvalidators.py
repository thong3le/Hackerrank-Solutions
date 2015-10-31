s = raw_input()
a = [False]*5
for i in range(len(s)):
    if s[i].isalnum():
        a[0] = True
    if s[i].isalpha():
        a[1] = True
    if s[i].isdigit():
        a[2] = True
    if s[i].islower():
        a[3] = True
    if s[i].isupper():
        a[4] = True

for i in a:
    print i