# Day 16 - CRUD Operations with FastAPI

## Overview

Day 16 focused on learning CRUD operations in FastAPI.

CRUD is the foundation of modern backend applications and is used to manage application data.

---

## Topics Covered

### Create

Used to create new data.

```http
POST /products
```

### Read

Used to retrieve data.

```http
GET /products
GET /products/{product_id}
```

### Update

Used to modify existing data.

```http
PUT /products/{product_id}
```

### Delete

Used to remove data.

```http
DELETE /products/{product_id}
```

---

## Project Built

### CRUD Product API

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
- Pydantic
- Uvicorn

---

## Concepts Practiced

- CRUD Operations
- REST APIs
- GET Requests
- POST Requests
- PUT Requests
- DELETE Requests
- Path Parameters
- Pydantic Models

---

## Run Project

```bash
uvicorn crud_product_api:app --reload
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

Day 16 helped me understand how real backend systems manage data through Create, Read, Update, and Delete operations. These concepts are fundamental for building scalable web applications, APIs, and future AI-powered products.