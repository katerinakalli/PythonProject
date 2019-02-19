import sys

x = int(input("Enter number of pronic numbers: "))

for i in range(1, x + 1):
    print(int(i * (i + 1)), end = ' ')
