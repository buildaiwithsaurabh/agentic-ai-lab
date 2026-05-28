# Definition of Property

# A property in Python is used to control access
# to instance variables using getter, setter,
# and deleter methods.

# It allows data encapsulation and validation.


# Example of Property in Python

class Student:

    def __init__(self, name):
        self.__name = name   # Private variable

    # Getter method
    @property
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, value):
        self.__name = value

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


# Creating object
s = Student("Rahul")

# Accessing property
print(s.name)

# Modifying property
s.name = "Aman"
print(s.name)

# Deleting property
del s.name


# Output:
# Rahul
# Aman