# ==========================================
# PYDANTIC MODELS
# ==========================================

# Definition:
#
# Pydantic is used for:
#
# - Data Validation
# - Type Checking
# - Request Parsing
#
# It ensures incoming data follows
# the required structure.


from pydantic import BaseModel


class Product(BaseModel):

    name: str
    category: str
    price: float
    in_stock: bool


product = Product(
    name="Laptop",
    category="Electronics",
    price=50000,
    in_stock=True
)

print(product)


# Benefits:
#
# ✓ Validation
# ✓ Type Safety
# ✓ Automatic Documentation
# ✓ Cleaner Code