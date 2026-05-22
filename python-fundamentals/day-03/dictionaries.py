# DICTIONARIES IN PYTHON

# Definition:
# A dictionary is a collection of key-value pairs.
# Dictionaries are ordered, changeable, and do not allow duplicate keys.

# Dictionaries use curly braces {}



# ==========================================
# CREATING A DICTIONARY
# ==========================================

student = {
    "name": "Saurabh",
    "age": 21,
    "course": "Python"
}

print(student)



# ==========================================
# ACCESSING VALUES
# ==========================================

print(student["name"])      # Saurabh
print(student["age"])       # 21



# ==========================================
# USING get()
# ==========================================

# Safer way to access values

print(student.get("course"))

# If key does not exist
print(student.get("city"))      # None



# ==========================================
# ADDING NEW ITEMS
# ==========================================

student["city"] = "Delhi"

print(student)



# ==========================================
# UPDATING VALUES
# ==========================================

student["age"] = 22

print(student)



# ==========================================
# REMOVING ITEMS
# ==========================================

student.pop("city")

print(student)



# ==========================================
# LOOPING THROUGH DICTIONARY
# ==========================================

for key, value in student.items():
    print(key, ":", value)



# ==========================================
# DICTIONARY METHODS
# ==========================================

print(student.keys())       # All keys
print(student.values())     # All values
print(student.items())      # Key-value pairs



# ==========================================
# REAL-WORLD EXAMPLE
# ==========================================

product = {
    "name": "Laptop",
    "price": 55000,
    "brand": "HP",
    "in_stock": True
}

print("Product Name:", product["name"])
print("Price:", product["price"])



# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. Dictionaries store data in key-value pairs
# 2. Keys must be unique
# 3. Values can be duplicated
# 4. Dictionaries are mutable (changeable)
# 5. Access values using keys


# Syntax:
# dictionary = {
#     key : value
# }