# Definition of Exception Handling

# Exception handling is a process used to handle runtime errors
# so that the program does not crash.

# Python uses:
# try
# except
# else
# finally


# Example 1: Basic Exception Handling

try:
    num1 = 10
    num2 = 0

    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# Output:
# Cannot divide by zero



# Example 2: Using else Block

try:
    num = 10

    print(num)

except:
    print("Error occurred")

else:
    print("Program executed successfully")


# Output:
# 10
# Program executed successfully



# Example 3: Using finally Block

try:
    file = open("sample.txt", "r")

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed")


# Output:
# File not found
# Execution completed



# Example 4: Handling Multiple Exceptions

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Invalid input")


# Example Output:
# Division by zero is not allowed
# OR
# Invalid input