from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# ==========================================
# PYDANTIC MODEL
# ==========================================

class Product(BaseModel):

    name: str
    category: str
    price: float


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():

    conn = sqlite3.connect("products.db")

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Product CRUD API"
    }


# ==========================================
# CREATE PRODUCT
# ==========================================

@app.post("/products")
def create_product(product: Product):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products (name, category, price)
    VALUES (?, ?, ?)
    """, (
        product.name,
        product.category,
        product.price
    ))

    conn.commit()

    conn.close()

    return {
        "message": "Product Created Successfully"
    }


# ==========================================
# GET ALL PRODUCTS
# ==========================================

@app.get("/products")
def get_products():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return [dict(product) for product in products]


# ==========================================
# GET PRODUCT BY ID
# ==========================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    )

    product = cursor.fetchone()

    conn.close()

    if product:

        return dict(product)

    return {
        "error": "Product Not Found"
    }


# ==========================================
# UPDATE PRODUCT
# ==========================================

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE products
    SET name = ?, category = ?, price = ?
    WHERE id = ?
    """, (
        product.name,
        product.category,
        product.price,
        product_id
    ))

    conn.commit()

    conn.close()

    return {
        "message": "Product Updated Successfully"
    }


# ==========================================
# DELETE PRODUCT
# ==========================================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    conn.commit()

    conn.close()

    return {
        "message": "Product Deleted Successfully"
    }


# ==========================================
# RUN PROJECT
# ==========================================

# Step 1
# python database_setup.py
#
# Step 2
# uvicorn product_crud_api:app --reload
#
# Swagger Docs:
#
# http://127.0.0.1:8000/docs