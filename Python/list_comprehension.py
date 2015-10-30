X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

result = []
for i in range(X+1):
    for j in range(Y+1):
        for k in range(Z+1):
            if i+j+k != N:
                result.append([i,j,k])

print result