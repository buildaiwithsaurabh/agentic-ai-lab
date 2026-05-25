# List Comprehension in Python

# Syntax:
# [expression for item in iterable]


# 1. Basic Example
numbers = [1, 2, 3, 4, 5]

square = [num * num for num in numbers]

print(square)


# 2. Convert to Uppercase
names = ["aman", "raj", "rohit"]

upper_names = [name.upper() for name in names]

print(upper_names)


# 3. Even Numbers
nums = [1, 2, 3, 4, 5, 6]

even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)


# 4. Odd Numbers
odd_nums = [num for num in nums if num % 2 != 0]

print(odd_nums)


# 5. Length of Words
words = ["apple", "banana", "mango"]

lengths = [len(word) for word in words]

print(lengths)


# 6. Create List using range()
numbers = [x for x in range(1, 11)]

print(numbers)


# 7. Squares using range()
squares = [x * x for x in range(1, 6)]

print(squares)


# 8. Conditional Expression
result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]

print(result)


# 9. Nested List Comprehension
matrix = [[j for j in range(3)] for i in range(3)]

print(matrix)


# 10. Traditional Loop vs List Comprehension

# Traditional Loop
square_list = []

for num in numbers:
    square_list.append(num * num)

print(square_list)

# List Comprehension
square_list2 = [num * num for num in numbers]

print(square_list2)