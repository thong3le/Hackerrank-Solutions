from math import sqrt

class Complex(object):
    def __init__(self,real = 0.0, im = 0.0):
        self.r = real
        self.i = im

    def __add__(self,c):
        return Complex(self.r + c.r, self.i + c.i)

    def __sub__(self,c):
        return Complex(self.r - c.r, self.i - c.i)

    def __mul__(self,c):
        return Complex(self.r*c.r - self.i*c.i, self.r*c.i + self.i*c.r) 

    def __div__(self,c):
        return Complex((self.r*c.r+self.i*c.i)/(c.r**2+c.i**2), (self.i*c.r-self.r*c.i)/(c.r**2+c.i**2))

    def __abs__(self):
        return "%.2f" % sqrt(self.r**2+self.i**2)

    def __str__(self):
        if self.i == 0:
            return "%.2f" % self.r
        elif self.r == 0:
            return "%.2fi" % self.i
        elif self.i < 0:
            return "%.2f - %.2fi" % (self.r, -self.i)
        elif self.i>0:
            return "%.2f + %.2fi" % (self.r, self.i)

a,b = map(float, raw_input().split())
c1 = Complex(a,b)
a,b = map(float, raw_input().split())
c2 = Complex(a,b)

print c1 + c2
print c1 - c2
print c1 * c2
print c1 / c2
print abs(c1)
print abs(c2)
