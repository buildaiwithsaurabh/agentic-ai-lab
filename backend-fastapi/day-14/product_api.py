# ==========================================
# PRODUCT API PROJECT
# ==========================================

# Problem Statement:
#
# Imagine you are building an e-commerce application
# like Amazon, Flipkart, or Myntra.
#
# Users should be able to:
#
# 1. View all products
# 2. View a specific product
# 3. Search products by category
#
# We will build these features using FastAPI.


# ==========================================
# REQUIREMENTS
# ==========================================

# Requirement 1:
# Get all products
#
# Endpoint:
# GET /products
#
# Example:
# http://127.0.0.1:8000/products


# Requirement 2:
# Get a specific product
#
# Endpoint:
# GET /products/{product_id}
#
# Example:
# http://127.0.0.1:8000/products/1
#
# Uses:
# Path Parameter


# Requirement 3:
# Search products by category
#
# Endpoint:
# GET /search?category=electronics
#
# Example:
# http://127.0.0.1:8000/search?category=electronics
#
# Uses:
# Query Parameter


# ==========================================
# IMPORT FASTAPI
# ==========================================

from fastapi import FastAPI

app = FastAPI()


# ==========================================
# SAMPLE PRODUCT DATA
# ==========================================

products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics",
        "price": 50000
    },
    {
        "id": 2,
        "name": "Phone",
        "category": "electronics",
        "price": 20000
    },
    {
        "id": 3,
        "name": "Shoes",
        "category": "fashion",
        "price": 3000
    }
]


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to Product API"
    }


# ==========================================
# GET ALL PRODUCTS
# ==========================================

@app.get("/products")
def get_products():

    return products


# Test URL:
#
# http://127.0.0.1:8000/products


# ==========================================
# GET PRODUCT BY ID
# ==========================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {
        "error": "Product not found"
    }


# Test URL:
#
# http://127.0.0.1:8000/products/1
#
# Uses:
# Path Parameter


# ==========================================
# SEARCH PRODUCTS BY CATEGORY
# ==========================================

@app.get("/search")
def search_products(category: str):

    filtered_products = []

    for product in products:

        if product["category"] == category:
            filtered_products.append(product)

    return filtered_products


# Test URL:
#
# http://127.0.0.1:8000/search?category=electronics
#
# Uses:
# Query Parameter


# ==========================================
# WHAT YOU LEARNED
# ==========================================

# ✓ FastAPI Routes
# ✓ API Endpoints
# ✓ Path Parameters
# ✓ Query Parameters
# ✓ Lists
# ✓ Dictionaries
# ✓ API Design
# ✓ Backend Fundamentals


# ==========================================
# RUN THE APPLICATION
# ==========================================

# Command:
#
# uvicorn product_api:app --reload


# Open:
#
# http://127.0.0.1:8000
#
# Swagger Docs:
#
# http://127.0.0.1:8000/docs