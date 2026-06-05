# ==========================================
# REQUEST BODY IN FASTAPI
# ==========================================

# Definition:
#
# A Request Body is data sent by the client
# to the server using a POST request.
#
# Most APIs use JSON data in the request body.


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


@app.post("/product")
def create_product(product: Product):

    return {
        "message": "Product Created",
        "product": product
    }


# Test in Swagger:
#
# POST /product
#
# {
#   "name": "Laptop",
#   "price": 50000
# }