# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
for _ in range(n):
    num = raw_input()
    digits = filter(lambda x: x and int(num) % x == 0 , map(int, num))
    print len(digits)
