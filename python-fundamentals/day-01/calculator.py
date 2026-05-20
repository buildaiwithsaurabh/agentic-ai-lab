# Python Calculator

operator = input ("Enter the operator (+ , - , * , /) : ")
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."

print(f"The result of {num1} {operator} {num2} is : {result}")













