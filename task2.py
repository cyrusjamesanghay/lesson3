#task2

number = [1,2,3]

answer = input("Do you want to clear the list? (yes or no) :")
if answer == "yes":
    number.clear()
elif answer == "no":
    userData = int(input("new data :"))
    number.append(userData)

print(number)