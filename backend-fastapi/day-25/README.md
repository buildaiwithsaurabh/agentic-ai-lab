# Day 25 - Current User API & Role-Based Authorization

## Overview

Day 25 focused on identifying the currently logged-in user and implementing role-based authorization using JWT authentication.

Users can:

- Register
- Login
- View Profile
- Access Admin Routes (if authorized)

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

Returns JWT token.

### Current User Profile

```http
GET /profile
```

Returns:

```json
{
    "username": "saurabh",
    "email": "saurabh@gmail.com",
    "role": "admin"
}
```

### Admin Route

```http
GET /admin
```

Accessible only to admin users.

---

## Technologies Used

- Python
- FastAPI
- SQLite
- JWT
- Passlib
- bcrypt
- python-jose

---

## Concepts Practiced

- JWT Authentication
- Current User Identification
- Token Validation
- Role-Based Access Control (RBAC)
- Admin Authorization

---

## Installation

```bash
pip install passlib[bcrypt]
pip install python-jose[cryptography]
```

---

## Run Project

```bash
python database_setup.py
```

```bash
uvicorn current_user_api:app --reload
```

---

## Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcome

Day 25 introduced role-based authorization and current-user identification using JWT tokens. These concepts are widely used in production SaaS applications to control access to resources and features.

---

## Next Step

Day 26:

- SQLAlchemy ORM
- Models
- Database Abstraction
- Professional Database Management