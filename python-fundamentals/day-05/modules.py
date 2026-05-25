# MODULES IN PYTHON

# Definition:
# A module is a Python file (.py) that contains
# variables, functions, classes, or code
# which can be reused in another Python file.


# Example:
# math.py
#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b


# Importing a Module

import math

print(math.sqrt(16))


# Import Specific Function

from math import sqrt

print(sqrt(25))


# Import Multiple Functions

from math import sqrt, factorial

print(sqrt(36))
print(factorial(5))


# Import with Alias

import math as m

print(m.pi)


# Custom Module Example

# calculator.py
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b


# main.py
#
# import calculator
#
# print(calculator.add(10, 20))
# print(calculator.multiply(5, 4))


# Module Benefits
#
# 1. Code Reusability
# 2. Better Organization
# 3. Easy Maintenance
# 4. Avoid Rewriting Code


# Types of Modules
#
# 1. Built-in Modules
#    Example: math, random, os
#
# 2. User-defined Modules
#    Modules created by users
#
# 3. External Modules
#    Installed using pip
#    Example: numpy, pandas


# Useful Built-in Modules

import random
import os
import datetime

print(random.randint(1, 10))

print(os.getcwd())

print(datetime.datetime.now())