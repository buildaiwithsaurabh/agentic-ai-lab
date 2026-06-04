# Product API

## Overview

This project is a simple Product API built using FastAPI.

The goal is to understand how APIs work and practice using Path Parameters and Query Parameters to retrieve and filter data.

---

## Problem Statement

Imagine you are building an e-commerce application like Amazon or Flipkart.

Users should be able to:

* View all products
* View a specific product
* Search products by category

This API provides these functionalities using FastAPI.

---

## Features

### Get All Products

```http
GET /products
```

Returns all available products.

---

### Get Product By ID

```http
GET /products/{product_id}
```

Example:

```http
GET /products/1
```

Uses Path Parameters.

---

### Search Products By Category

```http
GET /search?category=electronics
```

Uses Query Parameters.

---

## Technologies Used

* Python
* FastAPI
* Uvicorn

---

## Concepts Practiced

* FastAPI Routing
* REST APIs
* Path Parameters
* Query Parameters
* Lists & Dictionaries
* Backend Fundamentals

---

## Run Project

```bash
uvicorn product_api:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

Through this project, I learned how to build API endpoints, retrieve specific resources using Path Parameters, and filter data using Query Parameters in FastAPI.
