from sqlalchemy.orm import Session

from models.product import Product

# ==========================================
# CREATE PRODUCT
# ==========================================

def create_product(
    db: Session,
    name: str,
    price: float
):

    product = Product(
        name=name,
        price=price
    )

    db.add(product)

    db.commit()

    db.refresh(product)

    return product


# ==========================================
# GET ALL PRODUCTS
# ==========================================

def get_products(
    db: Session
):

    return db.query(
        Product
    ).all()