from fastapi import FastAPI

from config import APP_NAME

from database import Base
from database import engine

from routers.auth import router as auth_router
from routers.users import router as user_router

app = FastAPI(
    title=APP_NAME
)

Base.metadata.create_all(
    bind=engine
)

app.include_router(auth_router)

app.include_router(user_router)


@app.get("/")
def home():

    return {
        "message": APP_NAME
    }