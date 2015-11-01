import datetime

n = input()
mon = {'Jan': 1, 'Feb':2, 'Mar': 3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
for _ in range(n):
	t1 = raw_input().split()
	day1 = int(t1[1]); mon1 = mon[t1[2]]; year1 = int(t1[3])
	hour1, minute1, second1 = map(int, t1[4].split(':'))
	sign1 = t1[5][0]
	tz1 = int(t1[5][1:3])*3600 + int(t1[5][3:5])*60
	dt1 = datetime.datetime(year1, mon1, day1, hour1, minute1, second1)


	t2 = raw_input().split()
	
	day2 = int(t2[1]); mon2 = mon[t2[2]]; year2 = int(t2[3])
	hour2, minute2, second2 = map(int, t2[4].split(':'))
	sign2 = t2[5][0]
	tz2 = int(t2[5][1:3])*3600 + int(t2[5][3:5])*60
	dt2 = datetime.datetime(year2, mon2, day2, hour2, minute2, second2)

	ans = int((dt1-dt2).total_seconds())

	if sign1 == '-':
		ans += tz1
	else:
		ans -= tz1


	if sign2 == '-':
		ans -= tz2
	else:
		ans += tz2

	print abs(ans) 

