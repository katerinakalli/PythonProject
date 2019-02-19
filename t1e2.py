import sys

#This is input for 50s
print("Enter number of 50 euro banknotes: ")
fifties = input()
total = int(fifties) * 50

#This is input for 20s
print("Enter number of 20 euro banknotes: ")
twenties = input()
total = total + int(twenties) * 20

#This is input for 10s
print("Enter number of 10 euro banknotes: ")
tens = input()
total = total + int(tens) * 10

#This is input for 5s
print("Enter number of 5 euro banknotes: ")
fives = input()
total = total + int(fives) * 5

#This is input for 2s
print("Enter number of 2 euro coins: ")
twos = input()
total = total + int(twos) * 2

#This is input for 1s
print("Enter number of 1 euro coins: ")
ones = input()
total = total + int(ones)

print("Total is: ", total)
