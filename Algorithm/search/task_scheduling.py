from bisect import insort_left, bisect_left

def task_schedule(tasks, pos, max_pos, pre_max, m):
	if max_pos >=  pos and  pre_max > 0:
		return pre_max + m, max_pos + 1
	time = 0
	max_over = pre_max
	pos = 0
	for i in range(len(tasks)):
		d, t = tasks[i]
		time += t
		if max_over is None:
			max_over = time - d
		elif time - d  >= max_over:
			max_over = time - d
			pos = i
	return max_over, pos

n = input()

pre_max = None
max_pos = -1
tasks = []
for i in range(n):
	d, m = map(int, raw_input().strip().split())
	pos = bisect_left(tasks, (d,m))
	insort_left(tasks, (d, m))
	
	pre_max, max_pos = task_schedule(tasks, pos, max_pos, pre_max, m)

	print max(0, pre_max)
