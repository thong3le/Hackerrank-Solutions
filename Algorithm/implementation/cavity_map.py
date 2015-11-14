# Enter your code here. Read input from STDIN. Print output to STDOUT

def cavity(map):
    for i in range(1, len(map) - 1):
        for j in range(1, len(map) - 1):
            if map[i][j] > map[i-1][j] and map[i][j] > map[i+1][j] \
                and map[i][j] > map[i][j-1] and map[i][j] > map[i][j+1]:
                map[i][j] = 'X'
    return map

n = input()
map = []
for _ in range(n):
    map.append(list(raw_input()))
map = cavity(map)
for r in map:
    print ''.join(r)