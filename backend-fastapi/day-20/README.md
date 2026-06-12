# Day 20 - Inventory Management API

## Overview

Day 20 focused on building a complete Inventory Management API using FastAPI and SQLite.

This project combines all the backend concepts learned so far, including API development, database integration, CRUD operations, and data persistence.

---

## Problem Statement

Store owners need a system to manage inventory efficiently.

The application should allow users to:

- Add Products
- View Products
- Update Product Details
- Delete Products

This project provides a simple inventory management backend solution.

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

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Concepts Practiced

- CRUD Operations
- REST APIs
- Database Integration
- SQL Queries
- Data Persistence
- API Design

---

## Project Structure

```text
day-20/
│
├── database_setup.py
├── inventory_api.py
└── README.md
```

---

## Run Project

### Create Database

```bash
python database_setup.py
```

### Start API Server

```bash
uvicorn inventory_api:app --reload
```

---

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

This project helped me understand how real-world backend applications manage inventory using APIs and databases. It also strengthened my understanding of FastAPI, SQLite, and complete CRUD workflows.

---

## Next Step

Day 21:

- Authentication Fundamentals
- User Management Concepts
- Login & Registration Flow