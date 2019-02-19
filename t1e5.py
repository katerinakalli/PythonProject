import sys
import math
from fractions import Fraction

total = 0

#calculates the harmonic sequence
for i in range(1,6):
    total += 1 / i
    print(total)
