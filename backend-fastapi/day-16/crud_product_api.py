from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ==========================================
# PYDANTIC MODEL
# ==========================================

class Product(BaseModel):

    name: str
    category: str
    price: float


# ==========================================
# TEMPORARY DATABASE
# ==========================================

products = []


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "CRUD Product API"
    }


# ==========================================
# CREATE PRODUCT
# ==========================================

@app.post("/products")
def create_product(product: Product):

    products.append(product)

    return {
        "message": "Product Created Successfully",
        "product": product
    }


# ==========================================
# GET ALL PRODUCTS
# ==========================================

@app.get("/products")
def get_products():

    return products


# ==========================================
# GET PRODUCT BY ID
# ==========================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id < len(products):

        return products[product_id]

    return {
        "error": "Product Not Found"
    }


# ==========================================
# UPDATE PRODUCT
# ==========================================

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):

    if product_id < len(products):

        products[product_id] = updated_product

        return {
            "message": "Product Updated Successfully",
            "product": updated_product
        }

    return {
        "error": "Product Not Found"
    }


# ==========================================
# DELETE PRODUCT
# ==========================================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id < len(products):

        deleted_product = products.pop(product_id)

        return {
            "message": "Product Deleted Successfully",
            "product": deleted_product
        }

    return {
        "error": "Product Not Found"
    }


# ==========================================
# RUN PROJECT
# ==========================================

# uvicorn crud_product_api:app --reload


# Swagger Docs:
#
# http://127.0.0.1:8000/docs