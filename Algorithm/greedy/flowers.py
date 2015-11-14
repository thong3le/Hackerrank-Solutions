N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
    C.append( int(number) )
    i = i+1

C.sort(reverse = True)    
result = 0
for i in range(N):
    result += C[i]*(i//K + 1)

print result