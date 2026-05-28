# Definition of Magic Method

# Magic methods are special methods in Python
# that start and end with double underscores (__).

# They are also called Dunder Methods.

# These methods are automatically called
# when certain operations are performed on objects.


# Example of Magic Method

class Student:

    # Constructor Magic Method
    def __init__(self, name):
        self.name = name

    # String Representation Magic Method
    def __str__(self):
        return f"Student Name: {self.name}"


# Creating object
s = Student("Rahul")

# Printing object
print(s)


# Output:
# Student Name: Rahul

# More Examples of Magic Methods in Python


# Example 1: __len__() Magic Method

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages


b = Book(250)

print("Total Pages =", len(b))


# Output:
# Total Pages = 250



# Example 2: __add__() Magic Method

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print("Addition =", n1 + n2)


# Output:
# Addition = 30



# Example 3: __gt__() Magic Method

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(85)
s2 = Student(75)

print(s1 > s2)


# Output:
# True



# Example 4: __del__() Magic Method

class Test:
    def __del__(self):
        print("Object Destroyed")


t = Test()

del t


# Output:
# Object Destroyed


