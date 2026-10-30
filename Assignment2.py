#A program to make a simple calculator

#user inputs

num1 = float(input("Enter First number:"))
num2 = float(input("Enter Second number:"))
operation = input("Enter operation(+,-,*,/,**,%):")

#operations
if operation == "+":
    print("Sum:",num1+num2)

elif operation == "-":
    print("Difference:",num1-num2)

elif operation == "*":
    print("Multiplication:",num1*num2)

elif operation == "/":
    print("Division:",num1/num2)

elif operation == "**":
    print("Exponent:",num1**num2)

elif operation == "%":
    print("Remainder:",num1/num2)

else:
    print("Operation not supported!!")
