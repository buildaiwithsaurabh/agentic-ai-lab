# Function Arguments in Python

# An argument preceded by an identifier helps with readability.
# Order of arguments does not matter.

# 1. Positional Arguments

def greet(name, age):
    print(f"Hello {name}")
    print(f"You are {age} years old")

greet("Ali", 20)


# 2. Default Arguments

def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Ali")


# 3. Keyword Arguments

def student(name, age):
    print(name)
    print(age)

student(age=20, name="Ali")


# 4. Arbitrary Arguments (*args)

def add(*numbers):

    total = 0

    for num in numbers:
        total += num

    print(total)

add(1, 2, 3)
add(5, 10, 20, 30)


# 5. Arbitrary Keyword Arguments (**kwargs)

def info(**data):

    for key, value in data.items():
        print(key, value)

info(name="Ali", age=20)