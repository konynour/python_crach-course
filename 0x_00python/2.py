# 2. Write a program that asks the user for their name and age, 
# then prints out a message addressed to them that tells them the year that they will turn 100 years old.
name=input("your name:")
while_name=""
print("you didn`t Enter your name")
name=input("Enter your name:")
print(f"hello {name}")
age=int(input("enter your age:"))
print("************************************************************************************")
while age<=0:
    age=int(input("enter your age :"))
else:
    print(f":your {age} years old")
food=input("enter the food what you love it:")
print("************************************************************************************")
while not food=="q":
    print(f"ypu loike {food}")
    food=input("enter another food you like it:(q to quit)")
    print("bye")