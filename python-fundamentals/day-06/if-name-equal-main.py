# if __name__ == "__main__"

# Definition:
# The if __name__ == "__main__" statement is used
# to check whether a Python file is being run directly
# or imported as a module into another file.


# Why it is used:
# - Prevents certain code from running when imported
# - Allows functions/classes to be reused
# - Keeps code organized and modular


# How it works:

# When a Python file runs directly:
# __name__ becomes "__main__"

# When a Python file is imported:
# __name__ becomes the filename/module name


# Syntax:

def main():
    # Main program code goes here
    print("Program is running directly")


if __name__ == "__main__":
    main()


# Output when run directly:
# Program is running directly


# Example:

# file: math_utils.py

def add(a, b):
    return a + b


def main():
    print(add(10, 20))


if __name__ == "__main__":
    main()


# If you run:
# python math_utils.py

# Output:
# 30


# But if imported:

# import math_utils

# The main() function will NOT execute automatically.


# Benefits:
# 1. Code reusability
# 2. Better project structure
# 3. Prevents unwanted execution
# 4. Useful for testing and modules