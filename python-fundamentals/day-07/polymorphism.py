# Definition of Polymorphism

# Polymorphism is a feature of Object-Oriented Programming (OOP)
# where one method or function can have many forms.

# The same function name can perform different tasks
# depending on the object.


# Example of Polymorphism in Python

class Bird:
    def sound(self):
        print("Birds make sounds")


class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")


class Crow(Bird):
    def sound(self):
        print("Crow caws")


# Creating objects
s = Sparrow()
c = Crow()

# Calling same method with different behavior
s.sound()
c.sound()


# Output:
# Sparrow chirps
# Crow caws