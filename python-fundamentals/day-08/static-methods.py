# Definition of Static Method

# A static method is a method that belongs to the class
# rather than the object of the class.

# It does not use:
# self (object reference)
# cls (class reference)

# Static methods are created using @staticmethod decorator.


# Example of Static Method in Python

class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b


# Calling static method using class name
result = MathOperations.add(10, 20)

print("Sum =", result)


# Output:
# Sum = 30


# Example 1: Static Method for Temperature Conversion

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# Calling static method
temp = Temperature.celsius_to_fahrenheit(25)

print("Temperature in Fahrenheit =", temp)


# Output:
# Temperature in Fahrenheit = 77.0

# Example 2: Static Method for Even or Odd

class Number:

    @staticmethod
    def check(num):
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")


# Calling static method
Number.check(10)
Number.check(7)


# Output:
# 10 is Even
# 7 is Odd

# Example 3: Static Method Without Creating Object

class Employee:

    @staticmethod
    def company():
        print("Company Name: OpenAI")


# Calling static method directly using class name
Employee.company()


# Output:
# Company Name: OpenAI

# Example 4: Static Method with Calculator

class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


print("Multiplication =", Calculator.multiply(5, 4))
print("Division =", Calculator.divide(20, 5))


# Output:
# Multiplication = 20
# Division = 4.0