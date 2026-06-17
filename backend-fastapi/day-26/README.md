# Day 26 - SQLAlchemy ORM Fundamentals

## Overview

Day 26 focused on learning SQLAlchemy ORM, the most popular ORM used with FastAPI.

ORM stands for Object Relational Mapping.

Instead of writing raw SQL queries, SQLAlchemy allows developers to interact with databases using Python classes and objects.

---

## What is ORM?

Traditional SQL:

```sql
SELECT * FROM users;
```

SQLAlchemy ORM:

```python
users = db.query(User).all()
```

---

## Files

### database.py

Contains:

- Database Engine
- Session Configuration
- Base Class

### models.py

Contains:

- User Model
- Table Definitions
- Database Schema

### sqlalchemy_basics.py

Demonstrates:

- Create Tables
- Insert Data
- Query Data
- Database Sessions

---

## Technologies Used

- Python
- SQLite
- SQLAlchemy ORM

---

## Installation

```bash
pip install sqlalchemy
```

---

## Run Project

```bash
python sqlalchemy_basics.py
```

---

## Concepts Practiced

- ORM Fundamentals
- Database Engine
- Sessions
- Models
- Tables
- Insert Records
- Query Records

---

## Project Structure

```text
day-26/
│
├── database.py
├── models.py
├── sqlalchemy_basics.py
└── README.md
```

---

## Learning Outcome

Day 26 introduced SQLAlchemy ORM and demonstrated how Python classes can represent database tables.

This approach is widely used in professional FastAPI applications and helps developers build scalable backend systems.

---

## Next Step

Day 27:

- FastAPI + SQLAlchemy
- CRUD Operations
- API Integration
- Professional Database Workflows