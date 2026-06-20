from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.user_schema import (
    UserCreate,
    UserLogin
)

from models.user import User

from services.auth_service import (
    hash_password,
    verify_password,
    create_token
)

from services.user_service import (
    get_user_by_email
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:

        return {
            "error": "Email already exists"
        }

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    return {
        "message": "User Registered"
    }


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = get_user_by_email(
        db,
        user.email
    )

    if not db_user:

        return {
            "error": "User Not Found"
        }

    if not verify_password(
        user.password,
        db_user.password
    ):

        return {
            "error": "Invalid Password"
        }

    token = create_token(
        db_user.email
    )

    return {
        "access_token": token
    }