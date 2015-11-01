n = input()
s = set(map(int, raw_input().split())) 
N = input()
for _ in range(N):
    cmd = raw_input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
print sum(s)