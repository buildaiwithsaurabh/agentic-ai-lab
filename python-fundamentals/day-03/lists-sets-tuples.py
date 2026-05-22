# LISTS, SETS, AND TUPLES IN PYTHON


# ==========================================
# LIST
# ==========================================

# Definition:
# A list is an ordered and changeable collection.
# Allows duplicate values.

# Lists use square brackets []


fruits = ["apple", "banana", "orange", "banana"]

print(fruits)

# Access element
print(fruits[0])        # apple

# Modify element
fruits[1] = "mango"

# Add element
fruits.append("grapes")

# Remove element
fruits.remove("orange")

print(fruits)


# Features of Lists:
# 1. Ordered
# 2. Mutable (changeable)
# 3. Allows duplicates
# 4. Uses indexing


# ==========================================
# SET
# ==========================================

# Definition:
# A set is an unordered and immutable collection.
# Does NOT allow duplicate values.

# Sets use curly braces {}


cars = {"BMW", "Audi", "Tesla", "BMW"}

print(cars)

# Add element
cars.add("Mercedes")

# Remove element
cars.remove("Audi")

print(cars)


# Features of Sets:
# 1. Unordered
# 2. No duplicates
# 3. Faster lookups
# 4. No indexing


# ==========================================
# TUPLE
# ==========================================

# Definition:
# A tuple is an ordered but unchangeable collection.
# Allows duplicate values.

# Tuples use parentheses ()


colors = ("red", "green", "blue", "red")

print(colors)

# Access element
print(colors[1])        # green


# Features of Tuples:
# 1. Ordered
# 2. Immutable (cannot change)
# 3. Allows duplicates
# 4. Faster than lists


# ==========================================
# DIFFERENCE SUMMARY
# ==========================================

# LIST
# ----
# Ordered       -> Yes
# Mutable       -> Yes
# Duplicates    -> Yes
# Indexing      -> Yes


# SET
# ---
# Ordered       -> No
# Mutable       -> Yes
# Duplicates    -> No
# Indexing      -> No


# TUPLE
# -----
# Ordered       -> Yes
# Mutable       -> No
# Duplicates    -> Yes
# Indexing      -> Yes