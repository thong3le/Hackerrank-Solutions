from cmath import sqrt, acos, pi

class Point3D(object):
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		self.x = x
		self.y = y
		self.z = z
	
	def cross(self, other):
		return Point3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

	def __sub__(self, other):
		return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

	def __abs__(self):
		return sqrt(self.x ** 2 + self.y ** 2 + self.z **2)

	def dot(self, other):
		return (self.x * other.x + self.y * other.y + self.z * other.z)

	def __str__(self):
		return "(%.2f, %.2f, %.2f)" % (self.x, self.y, self.z)


x, y, z = map(float, raw_input().split())
A = Point3D(x, y, z)

x, y, z = map(float, raw_input().split())
B = Point3D(x, y, z)

x, y, z = map(float, raw_input().split())
C = Point3D(x, y, z)

x, y, z = map(float, raw_input().split())
D = Point3D(x, y, z)

AB = B - A
BC = C - B
CD = D - C

X = AB.cross(BC)
Y = BC.cross(CD)

print "%.2f" % ((acos(X.dot(Y) / (abs(X)*abs(Y)))).real*180 / pi)
