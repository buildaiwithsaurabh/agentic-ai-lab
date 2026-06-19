from pydantic import BaseModel

# ==========================================
# PRODUCT CREATE
# ==========================================

class ProductCreate(BaseModel):

    name: str
    price: float


# ==========================================
# PRODUCT RESPONSE
# ==========================================

class ProductResponse(BaseModel):

    id: int
    name: str
    price: float

    class Config:

        from_attributes = True