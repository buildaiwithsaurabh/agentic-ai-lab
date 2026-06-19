from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.product_schema import ProductCreate

from services.product_service import (
    create_product,
    get_products
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# ==========================================
# CREATE PRODUCT
# ==========================================

@router.post("/")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    return create_product(
        db,
        product.name,
        product.price
    )


# ==========================================
# GET PRODUCTS
# ==========================================

@router.get("/")
def all_products(
    db: Session = Depends(get_db)
):

    return get_products(db)