# Definition of Decorator

# A decorator in Python is a function
# that modifies the behavior of another function
# without changing its original code.

# Decorators are represented using @ symbol.


# Example of Decorator in Python

# Decorator function
def my_decorator(func):

    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


# Applying decorator
@my_decorator
def message():
    print("Hello Python")


# Calling function
message()


# Output:
# Before function call
# Hello Python
# After function call

# More Examples of Decorators in Python


# Example 1: Simple Decorator

def greeting_decorator(func):

    def wrapper():
        print("Welcome")
        func()
        print("Thank You")

    return wrapper


@greeting_decorator
def say_hello():
    print("Hello User")


say_hello()


# Output:
# Welcome
# Hello User
# Thank You



# Example 2: Decorator with Arguments

def smart_divide(func):

    def wrapper(a, b):

        if b == 0:
            print("Cannot divide by zero")
            return

        return func(a, b)

    return wrapper


@smart_divide
def divide(a, b):
    print(a / b)


divide(10, 2)
divide(10, 0)


# Output:
# 5.0
# Cannot divide by zero



# Example 3: Multiple Decorators

def star(func):

    def wrapper():
        print("*" * 20)
        func()
        print("*" * 20)

    return wrapper


def hash_symbol(func):

    def wrapper():
        print("#" * 20)
        func()
        print("#" * 20)

    return wrapper


@star
@hash_symbol
def display():
    print("Python Decorators")


display()


# Output:
# ********************
# ####################
# Python Decorators
# ####################
# ********************