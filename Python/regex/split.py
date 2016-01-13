# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for w in re.split("[,.]", raw_input()):
    if w:
        print w