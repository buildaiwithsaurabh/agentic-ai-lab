from passlib.context import CryptContext
from jose import jwt

from config import SECRET_KEY
from config import ALGORITHM

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_token(email: str):

    return jwt.encode(
        {"email": email},
        SECRET_KEY,
        algorithm=ALGORITHM
    )