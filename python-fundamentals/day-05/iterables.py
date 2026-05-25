# Iterables = An object/collection that can return it's element one at a time , allowing it to be iterated over in a  loop

# Iterable in Python

# An iterable is any object you can loop through using a for loop.


# 1. List
numbers = [1, 2, 3]

for num in numbers:
    print(num)


# 2. Tuple
data = (10, 20, 30)

for item in data:
    print(item)


# 3. String
name = "Sush"

for ch in name:
    print(ch)


# 4. Dictionary
student = {
    "name": "Sush",
    "age": 22
}

# Loop through keys
for key in student:
    print(key)

# Loop through key-value pairs
for key, value in student.items():
    print(key, value)


# 5. Set
colors = {"red", "blue", "green"}

for color in colors:
    print(color)


# 6. Range
for i in range(5):
    print(i)


# Iterable vs Iterator

nums = [1, 2, 3]

# Convert iterable into iterator
iterator = iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))