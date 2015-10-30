def digit_sum(n):
    s = 0;
    while n > 0:
        s += n%10
        n = n/10
    return s

fac_digit_sum = [1, 1]
num = 1
i = 2
while i <= 1000:
    num *= i
    fac_digit_sum.append(digit_sum(num))
    i += 1

#print digit_sum(1234)

n = int(raw_input())
for i in range(n):
    print fac_digit_sum[int(raw_input())]