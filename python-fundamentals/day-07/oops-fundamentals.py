# A class is a blueprint or template used to create objects in Object-Oriented Programming (OOP).
# It defines the properties (variables) and behaviors (methods/functions) that objects will have.

class Car:
    color = "Red"

    def drive(self):
        print("Car is moving")


# Object = An object is an instance of a class.
# It is a real entity created from the class and can use the properties and methods defined in the class.

mycar = Car()

# A class variable is a variable that is shared by all objects of a class.
# It is declared inside the class but outside any method.

# Class variables store data common to every object.

class Student:
    school = "ABC School"   # Class variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

# school → class variable
# name → instance variable

class Student:
    school = "ABC School"   # Class variable

    def __init__(self, name):
        self.name = name    # Instance variable

s1 = Student("Rahul")
s2 = Student("Aman")

print(s1.school, s1.name)
print(s2.school, s2.name)
