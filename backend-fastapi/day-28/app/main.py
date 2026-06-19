from fastapi import FastAPI

from config import APP_NAME

from database import engine
from database import Base

from routers.products import router as product_router

# ==========================================
# CREATE TABLES
# ==========================================

Base.metadata.create_all(
    bind=engine
)

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title=APP_NAME
)

# ==========================================
# ROUTERS
# ==========================================

app.include_router(
    product_router
)

# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message": APP_NAME
    }