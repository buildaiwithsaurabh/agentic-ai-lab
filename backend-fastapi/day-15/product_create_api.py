# ==========================================
# PRODUCT CREATE API
# ==========================================

# Problem Statement:
#
# Build a simple Product API.
#
# Users should be able to:
#
# 1. Create Products
# 2. View Products
#
# We will use:
#
# - POST Request
# - Request Body
# - Pydantic Model


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):

    name: str
    category: str
    price: float


products = []


@app.get("/")
def home():

    return {
        "message": "Welcome to Product API"
    }


@app.post("/products")
def create_product(product: Product):

    products.append(product)

    return {
        "message": "Product Created Successfully",
        "product": product
    }


@app.get("/products")
def get_products():

    return products


# Test:
#
# POST /products
#
# {
#   "name": "Laptop",
#   "category": "Electronics",
#   "price": 50000
# }
#
#
# GET /products
#
# Returns all products.