matrix = []
for _ in range(6):
    matrix.append(map(int, raw_input().split()))
res = -90
for i in range(4):
    for j in range(4):
        res = max(res, matrix[i][j]+ matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2])

print res