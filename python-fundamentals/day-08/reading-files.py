# Definition of Read File

# Reading a file means accessing and displaying
# the content stored inside a file.

# Python uses open() function with "r" mode
# for reading files.


# Example 1: Reading Entire File

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# Output:
# File content will be displayed



# Example 2: Reading File Line by Line

file = open("sample.txt", "r")

for line in file:

    print(line)

file.close()


# Output:
# Each line will be displayed one by one



# Example 3: Using readline()

file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()


# Output:
# First line
# Second line



# Example 4: Using readlines()

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# Output:
# ['Line 1', 'Line 2', 'Line 3']



# Example 5: Using with Statement

with open("sample.txt", "r") as file:

    content = file.read()

    print(content)


# Output:
# File content will be displayed

# More Examples of Reading Files in Python


# Example 1: Reading First 10 Characters

with open("sample.txt", "r") as file:

    content = file.read(10)

    print(content)


# Output:
# First 10 characters from file



# Example 2: Reading File Using Loop

with open("sample.txt", "r") as file:

    for line in file:

        print(line.strip())


# Output:
# Each line printed without extra spaces



# Example 3: Counting Number of Lines in File

with open("sample.txt", "r") as file:

    lines = file.readlines()

    print("Total Lines =", len(lines))


# Output:
# Total Lines = Number of lines in file



# Example 4: Searching Word in File

word = "Python"

with open("sample.txt", "r") as file:

    content = file.read()

    if word in content:

        print(word, "found in file")

    else:

        print(word, "not found")


# Output:
# Python found in file
# OR
# Python not found



# Example 5: Reading File and Converting to Uppercase

with open("sample.txt", "r") as file:

    content = file.read()

    print(content.upper())


# Output:
# FILE CONTENT IN UPPERCASE



# Example 6: Reading CSV File

with open("data.csv", "r") as file:

    for line in file:

        print(line.strip())


# Output:
# CSV file data displayed line by line