import sys
import math

a = float(input("Please enter the length of side A: "))
b = float(input("Please enter the length of side B: "))
c = float(input("Please enter the length of side C: "))
root = math.sqrt((a + b + c) * (b + c - a) * (a - b + c) *  ( a + b - c))
area = 0.25 * root
print(area)
