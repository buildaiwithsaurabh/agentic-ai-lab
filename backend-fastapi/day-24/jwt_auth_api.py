from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
import sqlite3

app = FastAPI()

# ==========================================
# CONFIGURATION
# ==========================================

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==========================================
# MODELS
# ==========================================

class User(BaseModel):

    username: str
    email: str
    password: str


class LoginUser(BaseModel):

    email: str
    password: str


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():

    conn = sqlite3.connect("users.db")

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# CREATE TOKEN
# ==========================================

def create_access_token(data: dict):

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ==========================================
# VERIFY TOKEN
# ==========================================

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "JWT Authentication API"
    }


# ==========================================
# REGISTER USER
# ==========================================

@app.post("/register")
def register_user(user: User):

    conn = get_db_connection()

    cursor = conn.cursor()

    hashed_password = pwd_context.hash(
        user.password
    )

    try:

        cursor.execute("""
        INSERT INTO users (
            username,
            email,
            password
        )
        VALUES (?, ?, ?)
        """, (
            user.username,
            user.email,
            hashed_password
        ))

        conn.commit()

        conn.close()

        return {
            "message": "User Registered Successfully"
        }

    except:

        conn.close()

        return {
            "error": "Email Already Exists"
        }


# ==========================================
# LOGIN USER
# ==========================================

@app.post("/login")
def login_user(user: LoginUser):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE email = ?
    """, (
        user.email,
    ))

    db_user = cursor.fetchone()

    conn.close()

    if not db_user:

        return {
            "error": "User Not Found"
        }

    valid_password = pwd_context.verify(
        user.password,
        db_user["password"]
    )

    if not valid_password:

        return {
            "error": "Invalid Password"
        }

    access_token = create_access_token(
        {
            "sub": db_user["email"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ==========================================
# PROTECTED ROUTE
# ==========================================

@app.get("/profile")
def get_profile(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_token(token)

    if not payload:

        return {
            "error": "Invalid Token"
        }

    return {
        "message": "Welcome User",
        "email": payload["sub"]
    }


# ==========================================
# RUN PROJECT
# ==========================================

# Step 1
# python database_setup.py
#
# Step 2
# pip install python-jose[cryptography]
# pip install passlib[bcrypt]
#
# Step 3
# uvicorn jwt_auth_api:app --reload
#
# Swagger:
# http://127.0.0.1:8000/docs