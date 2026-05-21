# Day 02 - Python Fundamentals

## Overview

In Day 02 of my Python learning journey, I explored core programming concepts focused on control flow, string manipulation, loops, conditional expressions, formatting, and beginner-friendly practical programs.

This session helped strengthen my understanding of Python syntax, logical thinking, and problem-solving fundamentals.

---

# Topics Covered

## 1. Compound Interest Calculator

Built a compound interest calculator using the formula:

```python
A = P(1 + r/n)^(nt)
```

### Concepts Practiced
- User input handling
- Type casting (`float`, `int`)
- Mathematical operators
- Exponential calculations
- Formatted output

---

## 2. Format Specifiers

Learned how to format values using Python f-strings.

### Topics Covered
- Decimal precision (`.2f`)
- Width allocation
- Zero padding
- Left/Right/Center alignment
- Sign formatting
- Comma separators

### Example

```python
print(f"{price:,.2f}")
```

Output:

```text
12,345.68
```

---

# 3. Logical Operators

Practiced Python logical operators:

- `OR`
- `AND`
- `NOT`

### Concepts Covered
- Multiple condition evaluation
- Boolean expressions
- Conditional weather examples
- Truthy and falsy values

---

# 4. Conditional Expressions (Ternary Operator)

Learned one-line conditional statements.

### Example

```python
print("Positive" if num > 0 else "Negative")
```

### Concepts Covered
- Inline conditions
- Cleaner conditional syntax
- Readable expressions

---

# 5. Username Validation Exercise

Created a basic username validation system.

### Validation Rules
- Username must not exceed 12 characters
- Username must not contain spaces
- Username must not contain digits

### Concepts Practiced
- String methods
- Conditional statements
- Input validation

---

# 6. String Indexing & Slicing

Learned how to access characters and portions of strings using indexing.

### Concepts Covered
- Positive indexing
- Slicing
- Step values

### Example

```python
credit_number[::3]
```

---

# 7. String Methods

Practiced commonly used Python string methods.

### Methods Explored
- `find()`
- `rfind()`
- `capitalize()`
- `upper()`
- `lower()`
- `isdigit()`
- `isalpha()`
- `replace()`

---

# 8. Weight Converter Program

Built a Python weight conversion program.

### Features
- Kilograms to Pounds conversion
- Pounds to Kilograms conversion
- User input validation

### Concepts Practiced
- Conditional statements
- Arithmetic operations
- User interaction

---

# 9. While Loops

Learned how `while` loops work in Python.

### Concepts Covered
- Loop conditions
- Iteration
- Infinite loops
- Counter-based loops

### Example

```python
while count <= 5:
    print(count)
```

---

# Key Learnings

- Improved understanding of Python control flow
- Practiced real-world beginner projects
- Learned string manipulation techniques
- Strengthened logical thinking and debugging skills
- Gained confidence with loops and conditions

---

# Technologies Used

- Python 3
- VS Code
- PowerShell

---

# Folder Structure

```text
day-02/
│
├── compoundInterest.py
├── logicalOperator.py
├── stringMethods.py
├── whileLoop.py
├── weightConverter.py
└── README.md
```

---

# Conclusion

Day 02 focused on building a strong foundation in Python fundamentals through hands-on coding exercises and mini projects. These concepts are essential building blocks for advanced programming, backend development, automation, and AI engineering.
