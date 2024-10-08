list = ["A","C","B","D"]

userdata = input ("Do you want to sort or  reverse the data :")
if userdata == "reverse":
    list.reverse()
elif userdata == "sort":
    list.sort()

print(list)
