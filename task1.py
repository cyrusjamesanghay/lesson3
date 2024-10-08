#task1
numbers = []
numberofdata = []

num = int(input("Enter a number on how many you want to input:"))
numberofdata.append(num)

for i in range(num):
    data = int(input("Enter a data :"))
    numbers.append(data)

print(numbers)

#task2

number = [1,2,3]

answer = input("Do you want to clear the list? (yes or no) :")
if answer == "yes":
    number.clear()
elif answer == "no":
    userData = int(input("new data :"))
    number.append(userData)

print(number)