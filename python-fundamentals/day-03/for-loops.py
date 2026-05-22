# FOR LOOP

# Definition:
# A for loop is used to iterate over a sequence
# (such as a string, list, tuple, range, etc.)
# and execute a block of code multiple times.


# Syntax:

# for variable in sequence:
#     code


# Example 1: Using range()

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# Example 2: Starting and ending range

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# Example 3: Increment by step value

for i in range(0, 10, 2):
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8


# Example 4: Loop through string

name = "Python"

for char in name:
    print(char)


# Example 5: Reverse loop

for i in range(5, 0, -1):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1


# Common Uses of for loop:
# 1. Repeating tasks fixed number of times
# 2. Traversing strings/lists
# 3. Iterating over data
# 4. Pattern printing
# 5. Processing collections


# Important:
# range(start, stop, step)

# start -> starting value
# stop  -> ending value (excluded)
# step  -> increment/decrement