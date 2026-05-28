# Definition of Class Method

# A class method is a method that works with the class
# rather than the object of the class.

# It uses 'cls' as the first parameter
# and is created using @classmethod decorator.


# Example of Class Method in Python

class Student:

    school = "ABC School"

    # Class method
    @classmethod
    def show_school(cls):
        print("School Name =", cls.school)


# Calling class method using class name
Student.show_school()


# Output:
# School Name = ABC School


# Example 1: Accessing Class Variable using Class Method

class Employee:

    company = "Tech Solutions"

    @classmethod
    def show_company(cls):
        print("Company Name =", cls.company)


Employee.show_company()


# Output:
# Company Name = Tech Solutions

# Example 2: Modifying Class Variable using Class Method

class Car:

    brand = "Toyota"

    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand


print("Before Change:", Car.brand)

Car.change_brand("Honda")

print("After Change:", Car.brand)


# Output:
# Before Change: Toyota
# After Change: Honda

# Example 3: Calling Class Method using Object

class Student:

    school = "ABC School"

    @classmethod
    def display(cls):
        print("School =", cls.school)


# Creating object
s = Student()

# Calling class method using object
s.display()


# Output:
# School = ABC School