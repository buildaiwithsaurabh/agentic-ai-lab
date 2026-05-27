# Multiple inheritance is a type of inheritance in which one child class inherits properties and methods from more than one parent class.

# It allows a class to use features of multiple classes.

# First parent class
class Father:
    def skills1(self):
        print("Father: Gardening")


# Second parent class
class Mother:
    def skills2(self):
        print("Mother: Cooking")


# Child class inheriting from both parents
class Child(Father, Mother):
    def skills3(self):
        print("Child: Programming")


# Creating object
c = Child()

# Calling methods
c.skills1()
c.skills2()
c.skills3()

# Output

# Father: Gardening
# Mother: Cooking
# Child: Programming