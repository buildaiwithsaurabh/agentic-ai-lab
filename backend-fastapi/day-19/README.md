# Day 19 - Complete Database CRUD API

## Overview

Day 19 focused on building a complete CRUD API using FastAPI and SQLite.

The API can now create, retrieve, update, and delete product data stored in a database.

This represents a complete backend workflow where API endpoints interact directly with a persistent database.

---

## Topics Covered

### Create

```http
POST /products
```

Creates a new product.

---

### Read

```http
GET /products
GET /products/{product_id}
```

Retrieves product data.

---

### Update

```http
PUT /products/{product_id}
```

Updates an existing product.

---

### Delete

```http
DELETE /products/{product_id}
```

Removes a product from the database.

---

## Project Built

### Product CRUD API

Features:

- Create Product
- View All Products
- View Product By ID
- Update Product
- Delete Product

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
- Database Integration
- SQL Queries
- REST APIs
- Data Persistence
- Pydantic Models

---

## Files

### database_setup.py

Creates:

- SQLite Database
- Products Table

### product_crud_api.py

Implements:

- POST Endpoint
- GET Endpoints
- PUT Endpoint
- DELETE Endpoint

---

## Run Project

### Create Database

```bash
python database_setup.py
```

### Start API

```bash
uvicorn product_crud_api:app --reload
```

---

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

Day 19 helped me understand how backend applications perform complete database operations using APIs. By combining FastAPI and SQLite, I built a fully functional CRUD system that stores and manages persistent data.

---

## Next Step

Day 20:

- Mini Backend Project
- Project Structure
- Real-World API Design