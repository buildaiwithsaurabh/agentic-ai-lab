# Definition of Duck Typing

# Duck typing is a concept in Python where
# the type or class of an object is less important
# than the methods and behavior it has.

# In simple words:
# "If it looks like a duck and behaves like a duck,
# then it is considered a duck."


# Example of Duck Typing

class Duck:
    def sound(self):
        print("Duck says Quack")


class Dog:
    def sound(self):
        print("Dog says Bark")


# Common function
def make_sound(animal):
    animal.sound()


# Creating objects
d = Duck()
dg = Dog()

# Passing objects
make_sound(d)
make_sound(dg)


# Output:
# Duck says Quack
# Dog says Bark