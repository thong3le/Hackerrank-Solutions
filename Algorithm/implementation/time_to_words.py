# Enter your code here. Read input from STDIN. Print output to STDOUT

h = input()
m = input()
name = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
      ]

maps = {}
for i in range(1, 21):
    maps[i] = name[i]
for i in range(21, 30):
    maps[i] = name[20] + ' ' + name[i-20]
    
if m == 0:
    print "{} o' clock".format(maps[h])
elif m == 1:
    print "one minute past {}".format(maps[h])
elif m == 15:
    print "quarter past {}".format(maps[h])
elif m < 30:
    print "{} minutes past {}".format(maps[m], maps[h])
elif m == 30:
    print "half past {}".format(maps[h])
elif m == 45:
    print "quarter to {}".format(maps[h+1])
elif m < 60:
    print "{} minutes to {}".format(maps[60 - m], maps[h+1])