class Bit:
	def __init__(self, n):
		self.size = n
		self.data = [0] * (n+1)

	def sum(self, i):
		s = 0
		while i > 0:
			s += self.data[i]
			i -= i & -i
		return s

	def add(self, i, x):
		while i < self.size:
			self.data[i] += x
			i += i & -i

M, N, Q = map(int, raw_input().strip().split())
actors = [0] * N
scence = [0] * M
bit = Bit(N)

a = map(int, raw_input().strip().split())
for i in range(N):
	actors[i] = a[i]
	scence[a[i]] += 1

for i in range(M):
	bit.add(scence[i] + 1, 1)

for _ in range(Q):
	action = map(int, raw_input().strip().split())
	if action[0] == 1:
		t = action[1]
		bit.add(scence[actors[t]]+1, -1)
		scence[actors[t]] -= 1
		bit.add(scence[actors[t]]+1, 1)
		actors[t] = action[2]
		t = action[2]
		bit.add(scence[t]+1, -1)
		scence[t] += 1	
		bit.add(scence[t]+1, 1)
	else:
		print bit.sum(action[1])
