# NESTED LOOP IN PYTHON

# Definition:
# A nested loop is a loop inside another loop.

# The inner loop executes completely
# for every single iteration of the outer loop.


# Syntax:

# for outer_loop:
#     for inner_loop:
#         code


# Example 1: Simple Nested Loop

for i in range(3):
    for j in range(3):
        print(j)

# Output:
# 0
# 1
# 2
# 0
# 1
# 2
# 0
# 1
# 2


# Example 2: Row and Column Pattern

rows = 3
cols = 4

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()

# Output:
# * * * *
# * * * *
# * * * *


# Example 3: Multiplication Table

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# Output:
# 1 2 3
# 2 4 6
# 3 6 9


# Important Points:
# 1. Outer loop controls rows
# 2. Inner loop controls columns
# 3. Commonly used for patterns and matrices


# Common Uses:
# 1. Pattern printing
# 2. Matrix operations
# 3. Tables
# 4. Grid systems
# 5. Game development