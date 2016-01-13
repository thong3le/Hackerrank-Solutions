# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()
for _ in range(n):
    if re.search(r'^[+-]?[0-9]*\.[0-9]+$', raw_input()):
        print True
    else:
        print False