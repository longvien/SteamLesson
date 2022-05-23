array = input("Enter a positive array (Ex: 1 2 3 4 6 ): ")
numbers = array.split()
max_number = -1
for number in numbers:
    max_number = max(max_number,int(number))
print("max number is: " + str(max_number))