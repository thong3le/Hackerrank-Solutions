# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()
for _ in range(n):
    s = raw_input()
    if s.count('#') == 0 or s[0] == '#':
        continue
    for c in re.findall(r'#[A-Fa-f0-9]{3,6}', s):
        print c