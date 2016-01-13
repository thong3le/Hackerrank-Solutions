class Person:
	def __init__(self, initial_age):
		if initial_age < 0:
			print 'This person is not valid, setting age to 0.'
			self.age = 0
		else:
			self.age = initial_age
	def amIOld(self):
		if self.age < 13:
			print 'You are young.'
		elif self.age < 18:
			print 'You are a teenager.'
		else:
			print 'You are old.'
	def yearPasses(self):
		self.age += 1

def main():
	T = input()
	for _ in range(T):
		age = input()
		p = Person(age)
		p.amIOld()
		for j in range(3):
			p.yearPasses();
		p.amIOld();
		print ""

if __name__ == '__main__':
	main()