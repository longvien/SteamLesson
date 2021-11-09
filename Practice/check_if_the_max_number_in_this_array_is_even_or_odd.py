array = input("Enter a positive array (Ex: 1 2 3 4): ")
numbers = array.split()
max_number = -1
for number in numbers:
    max_number = max(max_number,int(number))

print("max number is: " + str(max_number))

if max_number%2 == 0:
    print("The max number in this array is even")
else:
    print("The max number in this array is odd")