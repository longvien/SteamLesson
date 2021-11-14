array = input("Enter an array. Ex: 1 2 3")
numbers = array.split()
for i in range(0,int(len(numbers)/2)):
    temp = numbers[len(numbers)-i-1]
    numbers[len(numbers)-i-1] = numbers[i]
    numbers[i] = temp
print(numbers)