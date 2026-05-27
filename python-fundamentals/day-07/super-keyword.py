# Definition of super() Keyword

# The super() keyword in Python is used to call methods
# or constructors of the parent class from the child class.

# It helps in:
# 1. Accessing parent class methods
# 2. Reusing parent class code
# 3. Avoiding direct use of parent class name


# Example 1: Using super() with Constructor

# Parent class
class Animal:
    def __init__(self):
        print("Animal Constructor")


# Child class
class Dog(Animal):
    def __init__(self):
        super().__init__()   # Calling parent constructor
        print("Dog Constructor")


# Creating object
d = Dog()


# Output:
# Animal Constructor
# Dog Constructor



# Example 2: Using super() with Method

class Parent:
    def show(self):
        print("Parent Method")


class Child(Parent):
    def show(self):
        super().show()   # Calling parent method
        print("Child Method")


# Creating object
c = Child()
c.show()


# Output:
# Parent Method
# Child Method