import cmath

ab = input()
bc = input()

angle = cmath.atan(float(ab)/bc)*180/cmath.pi

print str(int(round(angle.real))) + '°'