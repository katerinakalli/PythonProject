import sys
import math

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

#diakrinousa
d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
    print("The equation has two solutions: x1 = ", x1, ", x2 = ", x2)
elif d == 0:
    x1 = -b / (2 * a)
    print("The equation has 1 solution: Xo = ", x1)
else:
    print("The equation has no solutuions.")

