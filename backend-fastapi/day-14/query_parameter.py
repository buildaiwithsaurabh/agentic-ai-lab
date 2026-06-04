# ==========================================
# QUERY PARAMETERS IN FASTAPI
# ==========================================

from fastapi import FastAPI

app = FastAPI()

# Definition:
# Query Parameters are values passed after the ? symbol in a URL.
#
# They are commonly used for:
#
# - Filtering
# - Searching
# - Sorting
# - Pagination
#
# Example:
#
# /products?category=laptop
#
# Here:
# category=laptop
#
# is the Query Parameter.


# Example 1: Single Query Parameter

@app.get("/products")
def get_products(category: str):

    return {
        "category": category
    }


# Test URL:
#
# http://127.0.0.1:8000/products?category=laptop
#
# Output:
#
# {
#     "category": "laptop"
# }


# ==========================================
# MULTIPLE QUERY PARAMETERS
# ==========================================

@app.get("/search")
def search(q: str, page: int = 1):

    return {
        "query": q,
        "page": page
    }


# Test URL:
#
# http://127.0.0.1:8000/search?q=fastapi&page=2
#
# Output:
#
# {
#     "query": "fastapi",
#     "page": 2
# }


# Common Use Cases:
#
# /products?category=laptop
# /search?q=python
# /users?page=2
# /products?sort=price
#
# Used when filtering, searching,
# sorting, or paginating data.


# ==========================================
# DIFFERENCE BETWEEN PATH PARAMETERS
# AND QUERY PARAMETERS
# ==========================================

# Path Parameters:
#
# - Part of URL path
# - Identify specific resource
# - Usually required
#
# Example:
#
# /users/10
#
# Meaning:
# Get user with ID 10


# Query Parameters:
#
# - Passed after ? symbol
# - Filter or modify results
# - Usually optional
#
# Example:
#
# /users?page=2
#
# Meaning:
# Get users from page 2


# ==========================================
# RULE TO REMEMBER
# ==========================================

# Path Parameter
#
# -> What resource?


# Query Parameter
#
# -> How should I filter/search that resource?


# Examples:
#
# /products/10
#
# Get Product 10


# /products?category=laptop
#
# Get products filtered by category laptop