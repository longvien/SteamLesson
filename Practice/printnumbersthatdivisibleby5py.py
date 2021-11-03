array = input("Enter an array: Ex: 1 2 3 4 5. ")
numbers = array.split( )

for number in numbers:
    if int(number)%5 == 0:
        print(number + " ")