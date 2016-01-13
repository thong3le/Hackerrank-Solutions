# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
consonant = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowel = 'AEIOUaeiou'
s = re.findall(r'(?<=[%s])([%s]{2,})(?=[%s])' % (consonant, vowel, consonant), raw_input())
if s:
    for w in s:
        print w
else:
    print -1