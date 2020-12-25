import datetime
now = datetime.datetime.now()
firstName = input("Please enter your name: ")
lastName = input("Please enter your surname: ")
age = int(input("Please enter your age: "))
dateOfBirth = int(input("Please enter your date of birth(Year): "))

userInfo = [firstName, lastName, age, dateOfBirth]
for i in userInfo:
    print(i)
if (now.year-userInfo[3] == userInfo[2]):
    if age >= 18:
        print("You can go out to the street")
    else:
        print("You can't go out because it's too dangerous")
else:
    print("Your age does not match your birth year")
