# Day 23 - User Login API

## Overview

Day 23 focused on building a User Login API using FastAPI, SQLite, and Password Verification.

Users can register accounts and securely log in using their email and password.

---

## Features

### Register User

```http
POST /register
```

Creates a new user account.

---

### Login User

```http
POST /login
```

Verifies:

- Email
- Password

Returns login success or failure.

---

### Get Users

```http
GET /users
```

Returns all registered users.

Passwords remain hidden.

---

## Technologies Used

- Python
- FastAPI
- SQLite
- Passlib
- bcrypt
- Pydantic

---

## Concepts Practiced

- User Registration
- User Login
- Password Hashing
- Password Verification
- Authentication Workflow
- Database User Lookup

---

## Authentication Flow

```text
Register User
      ↓
Hash Password
      ↓
Store User
      ↓
Login Request
      ↓
Find User
      ↓
Verify Password
      ↓
Login Successful
```

---

## Installation

```bash
pip install passlib[bcrypt]
```

---

## Run Project

### Create Database

```bash
python database_setup.py
```

### Start API

```bash
uvicorn user_login_api:app --reload
```

---

## Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

## Example Login Request

```json
{
    "email": "saurabh@gmail.com",
    "password": "admin123"
}
```

---

## Learning Outcome

Day 23 helped me understand how authentication systems verify user credentials. I learned how login APIs interact with databases, retrieve users, and validate passwords securely using hashing.

---

## Next Step

Day 24:

- JWT Authentication
- Access Tokens
- Protected Routes
- Authorization Header