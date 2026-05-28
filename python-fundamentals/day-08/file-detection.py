# Definition of File Detection

# File detection means checking whether a file exists
# or not before performing operations on it.

# Python provides the os module for file detection.


# Example 1: Checking File Exists or Not

import os

file_name = "sample.txt"

if os.path.exists(file_name):
    print("File exists")
else:
    print("File does not exist")


# Output:
# File exists
# OR
# File does not exist



# Example 2: Detecting File and Reading It

import os

file_name = "data.txt"

if os.path.isfile(file_name):

    file = open(file_name, "r")
    print(file.read())
    file.close()

else:
    print("File not found")


# Output:
# File content
# OR
# File not found

# More Examples of File Detection in Python


# Example 1: Checking Folder Exists or Not

import os

folder_name = "MyFolder"

if os.path.exists(folder_name):
    print("Folder exists")
else:
    print("Folder does not exist")


# Output:
# Folder exists
# OR
# Folder does not exist



# Example 2: Creating File if Not Exists

import os

file_name = "newfile.txt"

if not os.path.exists(file_name):

    file = open(file_name, "w")
    file.write("Hello Python")
    file.close()

    print("File created")

else:
    print("File already exists")


# Output:
# File created
# OR
# File already exists



# Example 3: Detecting Multiple Files

import os

files = ["a.txt", "b.txt", "c.txt"]

for file in files:

    if os.path.isfile(file):
        print(file, "exists")

    else:
        print(file, "not found")


# Example Output:
# a.txt exists
# b.txt not found
# c.txt exists



# Example 4: Using try-except with File Detection

file_name = "sample.txt"

try:

    file = open(file_name, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")


# Output:
# File content
# OR
# File not found