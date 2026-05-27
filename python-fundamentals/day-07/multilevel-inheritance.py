# Multilevel inheritance is a type of inheritance in which a class inherits from another class, and then another class inherits from that derived class.

# It forms a chain of inheritance.

# Grandparent class
class Grandfather:
    def show1(self):
        print("Grandfather Property")


# Parent class
class Father(Grandfather):
    def show2(self):
        print("Father Property")


# Child class
class Son(Father):
    def show3(self):
        print("Son Property")


# Creating object
s = Son()

# Calling methods
s.show1()
s.show2()
s.show3()

# Output

# Grandfather Property
# Father Property
# Son Property