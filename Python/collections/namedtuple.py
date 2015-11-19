from collections import namedtuple
n = input()
Student = namedtuple("Student", raw_input())
print sum( float(Student(*raw_input().split()).MARKS) for _ in range(n) ) / n

