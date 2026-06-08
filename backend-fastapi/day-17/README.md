# Day 17 - SQLite Database Fundamentals

## Overview

Day 17 focused on learning the fundamentals of databases using SQLite.

Until now, data was stored in Python lists, which disappear when the application stops running. SQLite provides a way to store data permanently in a database file.

This marks the beginning of working with real data storage systems used in backend development.

---

## Topics Covered

### What is a Database?

A database is a system used to store, organize, and retrieve data.

Examples:

- Users
- Products
- Orders
- Messages

---

### What is SQLite?

SQLite is a lightweight relational database built into Python.

Benefits:

- No installation required
- Easy to learn
- Fast and lightweight
- Stores data in a single file

---

## SQL Operations Learned

### Create Table

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);
```

### Insert Data

```sql
INSERT INTO products (name, price)
VALUES ('Laptop', 50000);
```

### Read Data

```sql
SELECT * FROM products;
```

### Update Data

```sql
UPDATE products
SET price = 55000
WHERE id = 1;
```

### Delete Data

```sql
DELETE FROM products
WHERE id = 1;
```

---

## Files

### sqlite_basics.py

Learned:

- Database Connection
- Cursor Object
- Table Creation
- Commit Changes
- Closing Connections

### product_database.py

Built a simple Product Database Manager with:

- Insert Product
- View Products
- Update Product
- Delete Product

---

## Technologies Used

- Python
- SQLite
- SQL

---

## Concepts Practiced

- Databases
- Tables
- Rows
- Columns
- SQL Queries
- CRUD Operations
- SQLite3 Module

---

## Run Project

### Create Database

```bash
python sqlite_basics.py
```

### Product Database Manager

```bash
python product_database.py
```

---

## Learning Outcome

Day 17 introduced database fundamentals and SQL operations using SQLite.

I learned how to create databases, manage tables, and perform CRUD operations on stored data. These concepts form the foundation for building backend applications that persist data reliably.

---

## Next Step

Day 18:

```text
FastAPI + SQLite
```

Building APIs that interact with a real database instead of temporary Python lists.