# FUNCTIONS IN PYTHON

# Definition:
# A function is a reusable block of code
# that performs a specific task.

# Functions help:
# 1. Reduce code repetition
# 2. Improve readability
# 3. Organize programs efficiently


# Syntax:

# def function_name(parameters):
#     code
#     return value


# ==========================================
# SIMPLE FUNCTION
# ==========================================

def greet():
    print("Hello, Welcome to Python!")

greet()



# ==========================================
# FUNCTION WITH PARAMETERS
# ==========================================

def greet_user(name):
    print(f"Hello {name}")

greet_user("Saurabh")



# ==========================================
# FUNCTION WITH RETURN VALUE
# ==========================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result)



# ==========================================
# FUNCTION WITH MULTIPLE PARAMETERS
# ==========================================

def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student("Saurabh", 21)



# ==========================================
# DEFAULT PARAMETERS
# ==========================================

def country(name="India"):
    print(f"Country: {name}")

country()
country("USA")



# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. Functions are reusable
# 2. 'def' keyword is used to create functions
# 3. Parameters receive values
# 4. return sends value back
# 5. Functions improve code modularity


# ==========================================
# COMMON USES
# ==========================================

# 1. Calculations
# 2. Data processing
# 3. User authentication
# 4. API handling
# 5. Automation