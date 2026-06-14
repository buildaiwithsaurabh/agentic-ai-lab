from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext
import sqlite3

app = FastAPI()


# ==========================================
# PASSWORD HASHING
# ==========================================

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
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "User Login API"
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

    password_match = pwd_context.verify(
        user.password,
        db_user["password"]
    )

    if not password_match:

        return {
            "error": "Invalid Password"
        }

    return {
        "message": "Login Successful"
    }


# ==========================================
# GET USERS
# ==========================================

@app.get("/users")
def get_users():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, username, email
    FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    return [dict(user) for user in users]


# ==========================================
# RUN PROJECT
# ==========================================

# Step 1
# python database_setup.py
#
# Step 2
# pip install passlib[bcrypt]
#
# Step 3
# uvicorn user_login_api:app --reload
#
# Swagger Docs:
#
# http://127.0.0.1:8000/docs