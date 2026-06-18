from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session

from database import engine
from database import get_db

from models import Base
from models import Product

from schemas import ProductCreate

app = FastAPI()

# ==========================================
# CREATE TABLES
# ==========================================

Base.metadata.create_all(
    bind=engine
)

# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Product Management API"
    }


# ==========================================
# CREATE PRODUCT
# ==========================================

@app.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = Product(
        name=product.name,
        price=product.price
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return {
        "message": "Product Created Successfully",
        "id": new_product.id
    }


# ==========================================
# GET ALL PRODUCTS
# ==========================================

@app.get("/products")
def get_products(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    return products


# ==========================================
# GET PRODUCT BY ID
# ==========================================

@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:

        return {
            "error": "Product Not Found"
        }

    return product


# ==========================================
# UPDATE PRODUCT
# ==========================================

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    updated_product: ProductCreate,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:

        return {
            "error": "Product Not Found"
        }

    product.name = updated_product.name
    product.price = updated_product.price

    db.commit()

    return {
        "message": "Product Updated Successfully"
    }


# ==========================================
# DELETE PRODUCT
# ==========================================

@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:

        return {
            "error": "Product Not Found"
        }

    db.delete(product)

    db.commit()

    return {
        "message": "Product Deleted Successfully"
    }


# ==========================================
# RUN PROJECT
# ==========================================

# pip install fastapi
# pip install uvicorn
# pip install sqlalchemy
#
# uvicorn product_api:app --reload
#
# http://127.0.0.1:8000/docs