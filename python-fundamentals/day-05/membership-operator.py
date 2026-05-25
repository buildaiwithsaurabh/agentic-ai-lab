# Membership Operators in Python

# in
# not in


# 1. List
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" not in fruits)


# 2. String
name = "Aman"

print("A" in name)
print("z" not in name)


# 3. Tuple
numbers = (1, 2, 3)

print(2 in numbers)
print(10 not in numbers)


# 4. Set
colors = {"red", "blue", "green"}

print("red" in colors)
print("yellow" not in colors)


# 5. Dictionary
student = {
    "name": "Aman",
    "age": 22
}

# checks keys
print("name" in student)

# checks values
print("Aman" in student.values())

# checks key-value pairs
print(("name", "Aman") in student.items())