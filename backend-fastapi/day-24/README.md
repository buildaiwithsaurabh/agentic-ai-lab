# Day 24 - JWT Authentication & Protected Routes

## Overview

Day 24 focused on implementing JWT Authentication using FastAPI.

Users can:

- Register
- Login
- Receive JWT Token
- Access Protected Routes

---

## Features

### Register User

```http
POST /register
```

### Login User

```http
POST /login
```

Returns:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

### Protected Route

```http
GET /profile
```

Requires JWT token.

---

## Technologies Used

- Python
- FastAPI
- SQLite
- JWT
- python-jose
- Passlib
- bcrypt

---

## Concepts Practiced

- Authentication
- Authorization
- JWT Tokens
- Access Tokens
- Protected Routes
- Password Hashing
- Token Validation

---

## Installation

```bash
pip install passlib[bcrypt]
pip install python-jose[cryptography]
```

---

## Run Project

### Create Database

```bash
python database_setup.py
```

### Start API

```bash
uvicorn jwt_auth_api:app --reload
```

---

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Authentication Flow

```text
Register User
      ↓
Login User
      ↓
Generate JWT
      ↓
Receive Token
      ↓
Access Protected Route
```

---

## Learning Outcome

Day 24 introduced JWT-based authentication and protected routes. I learned how tokens are generated, validated, and used to secure APIs.

---

## Next Step

Day 25:

- Current User API
- User Roles
- Authorization
- Admin vs User Access