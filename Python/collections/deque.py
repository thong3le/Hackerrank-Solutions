from collections import deque
n = input()
q = deque()
for _ in range(n):
    cmd = raw_input().strip().split()
    if cmd[0] == 'append':
        q.append(cmd[1])
    elif cmd[0] == 'appendleft':
        q.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        q.pop()
    elif cmd[0] == 'popleft':
        q.popleft()
print ' '.join(q)