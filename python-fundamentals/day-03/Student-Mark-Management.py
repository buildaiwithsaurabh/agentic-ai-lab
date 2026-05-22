# LIST PROGRAM
# Student Marks Management

marks = [85, 90, 78, 92]

print("Original Marks:", marks)

# Add new mark
marks.append(88)

# Remove mark
marks.remove(78)

# Update mark
marks[1] = 95

print("Updated Marks:", marks)

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))




# SET PROGRAM
# Unique Visitor Names

visitors = {"Saurabh", "Rahul", "Aman", "Saurabh"}

print("Visitors:", visitors)

# Add visitor
visitors.add("Priya")

# Remove visitor
visitors.remove("Rahul")

print("Updated Visitors:", visitors)

# Check visitor
if "Aman" in visitors:
    print("Aman visited")




# TUPLE PROGRAM
# Student Information

student = ("Saurabh", 21, "Python")

print("Student Details:", student)

# Access tuple elements
print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])

# Count occurrences
numbers = (1, 2, 3, 2, 4, 2)

print("Count of 2:", numbers.count(2))

# Find index
print("Index of 3:", numbers.index(3))