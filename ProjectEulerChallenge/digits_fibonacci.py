fib = [0,1]
digit_count = [1]
count = 2
for i in range(2, 3*10**4):
    fib.append(fib[i-1] + fib[i-2])
    if len(str(fib[i])) == count:
        digit_count.append(i)
        count+=1
        
#print len(digit_count)
n = int(raw_input())
for i in range(n):
    print digit_count[int(raw_input())-1]