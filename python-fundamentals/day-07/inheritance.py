# Inheritance is a feature of Object-Oriented Programming (OOP) in which one class acquires the properties and methods of another class.

# The existing class is called the Parent/Base class.
# The new class is called the Child/Derived class.

# Inheritance helps in:
#  Code reusability
#  Reducing duplication
#  Easy maintenance

# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")


# Creating object
d = Dog()

# Accessing parent class method
d.sound()

# Accessing child class method
d.bark()