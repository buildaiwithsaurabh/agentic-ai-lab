# Day 27 - FastAPI + SQLAlchemy CRUD API

## Overview

Day 27 focused on integrating FastAPI with SQLAlchemy ORM to build a complete Product Management API.

This project demonstrates professional backend architecture using:

- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic

---

## Features

### Create Product

```http
POST /products
```

### Get All Products

```http
GET /products
```

### Get Product By ID

```http
GET /products/{product_id}
```

### Update Product

```http
PUT /products/{product_id}
```

### Delete Product

```http
DELETE /products/{product_id}
```

---

## Project Structure

```text
day-27/
│
├── database.py
├── models.py
├── schemas.py
├── product_api.py
└── README.md
```

---

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Concepts Practiced

- ORM CRUD Operations
- Database Sessions
- Models
- Schemas
- Dependency Injection
- FastAPI Integration

---

## Installation

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
```

---

## Run Project

```bash
uvicorn product_api:app --reload
```

---

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

Day 27 introduced a professional FastAPI architecture using SQLAlchemy ORM. Instead of writing raw SQL queries, database operations are performed through Python models and ORM sessions.

This approach is commonly used in production-grade backend applications.

---

## Next Step

Day 28:

- Professional FastAPI Folder Structure
- Routers
- Services
- Dependency Injection
- Scalable Project Architecture