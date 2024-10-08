number = [1,2,3]

User = input("Do you want to remove an element by popo or remove :")
if User == "popo":
    choice2 = int(input("Enter a number :"))
    number.pop(choice2)
    print(choice2)
elif User == "remove":
    choice3 = int(input("Enter a data number :"))
    number.remove(choice3)

print(number)

