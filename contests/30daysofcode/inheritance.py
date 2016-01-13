class Student:
	def __init__(self, fn, ln, phone):
		self.fn = fn
		self.ln = ln
		self.phone = phone

	def display(self):
		print 'First Name: ', self.fn
		print 'Last Name: ', self.ln
		print 'Phone: ', self.phone

class Grade(Student):
	def __init__(self, fn, ln, phone, score):
		Student.__init__(self, fn, ln, phone)
		self.score = score

	def calculate(self):
		if self.score < 40:
			return 'D'
		elif self.score < 60:
			return 'B'
		elif self.score < 75:
			return 'A'
		elif self.score < 90:
			return 'E'
		else:
			return 'O'


fn = raw_input().strip()
ln = raw_input().strip()

phone = int(raw_input())
score = int(raw_input())

stu = Grade(fn, ln, phone, score)
stu.display()
print 'Grade: ', stu.calculate()