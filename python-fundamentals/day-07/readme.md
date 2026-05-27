# Day 07 - Python OOP Fundamentals

## Overview

Day 07 focused on understanding the core fundamentals of Object-Oriented Programming (OOP) in Python. I explored how classes and objects work, how inheritance enables code reusability, and how Python supports advanced OOP concepts like multiple inheritance, multilevel inheritance, `super()` keyword usage, and duck typing.

This session helped strengthen my understanding of writing scalable, reusable, and modular Python code.

---

# Topics Covered

## 1. Classes & Objects

Learned how classes act as blueprints for creating objects in Python.

### Concepts Practiced

- Creating classes
- Creating objects
- Defining methods
- Accessing attributes

### Example

```python
class Car:
    color = "Red"

    def drive(self):
        print("Car is moving")
```

---

# 2. Class Variables & Instance Variables

Explored the difference between:

- Class Variables → shared across all objects
- Instance Variables → unique for each object

### Concepts Practiced

- Shared data management
- Object-specific attributes
- Constructors (`__init__`)

### Example

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

---

# 3. Inheritance

Learned how child classes inherit properties and methods from parent classes.

### Benefits

- Code Reusability
- Reduced Duplication
- Better Maintainability

### Example

```python
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
```

---

# 4. Multilevel Inheritance

Explored inheritance chains where one class inherits from another derived class.

### Example Structure

```text
Grandfather → Father → Son
```

### Concepts Practiced

- Inheritance hierarchy
- Method inheritance
- Multi-level class relationships

---

# 5. Multiple Inheritance

Learned how one child class can inherit from multiple parent classes.

### Example Structure

```text
Father + Mother → Child
```

### Concepts Practiced

- Combining behaviors
- Accessing multiple parent methods
- OOP flexibility

---

# 6. super() Keyword

Learned how the `super()` keyword is used to access parent class constructors and methods.

### Benefits

- Reusing parent class logic
- Cleaner inheritance handling
- Avoiding direct parent class references

### Example

```python
super().__init__()
```

### Concepts Practiced

- Parent constructor calls
- Parent method access
- Method overriding

---

# 7. Duck Typing

Explored Python’s duck typing concept:

> “If it looks like a duck and behaves like a duck, it is considered a duck.”

### Concepts Practiced

- Dynamic typing
- Polymorphic behavior
- Method-based object handling

### Example

```python
def make_sound(animal):
    animal.sound()
```

Objects only need the required method, not a specific class type.

---

# Key Concepts Learned

- Object-Oriented Programming (OOP)
- Classes & Objects
- Constructors
- Class Variables
- Instance Variables
- Inheritance
- Multilevel Inheritance
- Multiple Inheritance
- Method Overriding
- `super()` Keyword
- Duck Typing

---

# Benefits of OOP

- Better Code Organization
- Reusability
- Scalability
- Easier Maintenance
- Real-World Modeling
- Cleaner Architecture

---

# Technologies Used

- Python 3
- VS Code
- PowerShell

---

# Folder Structure

```text
day-07/
│
├── classes_objects.py
├── class_instance_variables.py
├── inheritance.py
├── multilevel_inheritance.py
├── multiple_inheritance.py
├── super_keyword.py
├── duck_typing.py
└── README.md
```

---

# Key Takeaways

Day 07 helped me understand how large-scale applications are structured using Object-Oriented Programming principles.

These concepts are foundational for:
- Backend Development
- AI Engineering
- Software Architecture
- Automation Systems
- Scalable Applications

Understanding OOP deeply is an important step toward building production-grade software and real-world AI systems.

---

# Conclusion

Today’s learning focused on writing cleaner, reusable, and modular code using OOP concepts in Python.

By practicing inheritance, class structures, and object behavior, I’m building a stronger foundation for advanced software engineering and AI application development.
