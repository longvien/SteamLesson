import sys

array = input("Enter a positive array (Ex: 1 2 3 4): ")
numbers = array.split()
min_number = sys.maxsize
for number in numbers:
    min_number = min(min_number,int(number))
print("min_number is: " + str(min_number))