# 1. Write a Python program to calculate the sum of two numbers.
oprator =input("Enter the operator: (+, -, *, /): ")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if oprator== "+":
    result=num1+num2
    print(result)
elif oprator== "-":
    result=num1-num2
    print(result)
elif oprator== "*":
    result=num1*num2
    print(result)
elif oprator== "/":
    result=num1/num2
    print(result)
else:
    print("Invalid operator")        