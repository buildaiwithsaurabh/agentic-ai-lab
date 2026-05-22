# Day 03 - Python Fundamentals

## Overview

Day 03 focused on advancing my understanding of Python collections, loops, dictionaries, randomization, and beginner-friendly console applications.

Through hands-on coding exercises and mini projects, I strengthened my problem-solving abilities and learned how Python handles structured data and iterative programming.

---

# Topics Covered

## 1. For Loops

Learned how to iterate through sequences using Python `for` loops.

### Concepts Practiced
- `range()` function
- Start, stop, and step values
- Reverse iteration
- Iterating through strings
- Loop control

### Example

```python
for i in range(1, 6):
    print(i)
```

---

# 2. Lists, Sets, and Tuples

Explored Python collection data types and their differences.

## Lists
- Ordered
- Mutable
- Allows duplicates

## Sets
- Unordered
- No duplicate values
- Faster lookups

## Tuples
- Ordered
- Immutable
- Efficient for fixed data

### Concepts Practiced
- Adding/removing items
- Updating values
- Accessing elements
- Collection operations

---

# 3. Nested Loops

Learned how loops can exist inside other loops.

### Concepts Covered
- Row and column traversal
- Pattern printing
- Multiplication tables
- Matrix-style iteration

### Example

```python
for row in range(3):
    for col in range(3):
        print("*", end=" ")
```

---

# 4. 2D Collections

Practiced working with multidimensional collections.

### Topics Covered
- 2D Lists
- 2D Tuples
- Nested collections
- Table/grid-based data structures

### Real-World Example
- Tic-Tac-Toe board representation

---

# 5. Dictionaries

Learned how to store and manage data using key-value pairs.

### Concepts Practiced
- Creating dictionaries
- Accessing values
- Updating data
- Dictionary methods
- Looping through dictionaries

### Example

```python
student = {
    "name": "Saurabh",
    "age": 21
}
```

---

# 6. Random Module

Explored Python’s built-in `random` module.

### Functions Used
- `randint()`
- `random()`
- `choice()`
- `shuffle()`
- `randrange()`

### Applications
- Games
- Simulations
- Randomized outputs

---

# Mini Projects Built

## 1. Concession Stand Program

Built a simple food ordering console application.

### Features
- Menu system
- Cart management
- Total bill calculation
- User interaction

---

## 2. Number Guessing Game

Created an interactive guessing game using random numbers.

### Features
- Random number generation
- Input validation
- Hint system
- Guess counter

---

## 3. Quiz Game

Developed a console-based quiz application.

### Features
- Multiple questions
- Score tracking
- Conditional logic
- User feedback

---

## 4. Collection-Based Programs

Built small practice programs using:
- Lists
- Sets
- Tuples

### Example Projects
- Student marks management
- Unique visitor tracking
- Student information system

---

# Key Learnings

- Improved understanding of iteration and looping
- Learned how to manage structured data in Python
- Practiced real-world beginner-level projects
- Strengthened debugging and logical thinking
- Gained confidence with collections and nested data structures

---

# Technologies Used

- Python 3
- VS Code
- PowerShell

---

# Folder Structure

```text
day-03/
│
├── forLoops.py
├── collections.py
├── nestedLoops.py
├── dictionaries.py
├── randomNumbers.py
├── numberGuessingGame.py
├── quizGame.py
├── concessionStand.py
└── README.md
```

---

# Conclusion

Day 03 focused on building deeper programming fundamentals using loops, collections, dictionaries, and mini projects. These concepts are essential for backend development, automation, data handling, and future AI engineering projects.

```