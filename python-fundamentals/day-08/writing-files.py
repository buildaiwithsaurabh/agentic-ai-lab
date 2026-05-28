# Definition of Write File

# Writing a file means storing data into a file
# using Python file handling functions.

# Python uses open() function with different modes:
# "w" -> Write mode
# "a" -> Append mode


# Example 1: Writing Data into File

file = open("sample.txt", "w")

file.write("Hello Python\n")
file.write("Welcome to File Handling")

file.close()

print("Data written successfully")


# Output:
# Data written successfully



# Example 2: Reading Written File

file = open("sample.txt", "r")

print(file.read())

file.close()


# Output:
# Hello Python
# Welcome to File Handling



# Example 3: Using with Statement

with open("data.txt", "w") as file:

    file.write("Python File Handling Example")

print("File written successfully")


# Output:
# File written successfully



# Example 4: Appending Data into File

with open("sample.txt", "a") as file:

    file.write("\nThis line is appended")

print("Data appended successfully")


# Output:
# Data appended successfully


# More Examples of Writing Files in Python


# Example 1: Writing Multiple Lines

lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w") as file:

    file.writelines(lines)

print("Multiple lines written successfully")


# Output:
# Multiple lines written successfully



# Example 2: Taking User Input and Writing into File

name = input("Enter your name: ")

with open("user.txt", "w") as file:

    file.write("User Name: " + name)

print("User data saved")


# Example Output:
# User data saved



# Example 3: Writing Numbers into File

with open("numbers.txt", "w") as file:

    for i in range(1, 6):

        file.write(str(i) + "\n")

print("Numbers written successfully")


# Output:
# Numbers written successfully



# Example 4: Copying Content from One File to Another

with open("source.txt", "r") as source:

    content = source.read()

with open("destination.txt", "w") as destination:

    destination.write(content)

print("File copied successfully")


# Output:
# File copied successfully



# Example 5: Writing Dictionary Data into File

student = {
    "Name": "Rahul",
    "Age": 21,
    "Course": "Python"
}

with open("student.txt", "w") as file:

    for key, value in student.items():

        file.write(f"{key}: {value}\n")

print("Dictionary data written successfully")


# Output:
# Dictionary data written successfully