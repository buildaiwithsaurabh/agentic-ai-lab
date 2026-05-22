# 2D COLLECTIONS IN PYTHON

# Definition:
# A 2D collection is a collection inside another collection.
# Commonly used to store data in rows and columns.

# Examples:
# 1. List inside list
# 2. Tuple inside tuple
# 3. Set inside list


# ==========================================
# 2D LIST
# ==========================================

# Example: Student marks table

marks = [
    [85, 90, 78],
    [88, 76, 95],
    [92, 89, 84]
]

print(marks)

# Access specific element
print(marks[0][1])      # 90

# Access complete row
print(marks[1])

# Nested loop for printing rows and columns

for row in marks:
    for value in row:
        print(value, end=" ")
    print()


# Output:
# 85 90 78
# 88 76 95
# 92 89 84



# ==========================================
# 2D TUPLE
# ==========================================

# Example: Coordinates

coordinates = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(coordinates)

# Access element
print(coordinates[1][0])     # 3



# ==========================================
# 2D SET (using list of sets)
# ==========================================

# Sets themselves cannot contain sets directly
# because sets are mutable.

languages = [
    {"Python", "Java"},
    {"C++", "JavaScript"}
]

print(languages)

# Access set
print(languages[0])



# ==========================================
# REAL-WORLD EXAMPLE
# ==========================================

# Tic-Tac-Toe Board

board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", " ", "O"]
]

for row in board:
    for cell in row:
        print(cell, end=" ")
    print()


# Output:
# X O X
# O X O
# X   O



# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. 2D collections store data in tabular form
# 2. First index = row
# 3. Second index = column
# 4. Nested loops are commonly used


# Syntax:
# collection[row][column]