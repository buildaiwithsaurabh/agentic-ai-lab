# Day 18 - FastAPI + SQLite Integration

## Overview

Day 18 focused on connecting FastAPI with SQLite.

Previously, data was stored in Python lists and disappeared whenever the application restarted.

By integrating SQLite, data is now stored permanently inside a database.

---

## Topics Covered

### FastAPI

Built API endpoints using:

- GET
- POST

### SQLite

Worked with:

- Database Connections
- Tables
- SQL Queries

### Integration

Connected FastAPI endpoints directly to SQLite.

---

## Project Built

### Product API with SQLite

Features:

- Create Product
- Store Product in Database
- View All Products
- View Product By ID

---

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Concepts Practiced

- API Development
- Database Integration
- SQL Queries
- Data Persistence
- Request Body
- Pydantic Models

---

## Files

### database_connection.py

Creates:

- products.db
- products table

### product_api_sqlite.py

Implements:

- POST /products
- GET /products
- GET /products/{id}

---

## Run Project

### Create Database

```bash
python database_connection.py
```

### Start FastAPI

```bash
uvicorn product_api_sqlite:app --reload
```

---

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

Day 18 helped me understand how backend APIs communicate with databases.

This is a major step toward building production-ready backend systems where data persists even after the server restarts.

---

## Next Step

Day 19:

- Update Database Records
- Delete Database Records
- Complete Database CRUD API