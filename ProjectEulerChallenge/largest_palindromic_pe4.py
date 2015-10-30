palin = []
for i in range(101101, 1000000):
	if str(i) == str(i)[::-1]:
		for j in range(101, 1000):
			if i%j == 0 and len(str(i/j)) == 3:
				palin.append(i) 
				break
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print [p for p in palin if p <= n][-1]