# Day 22 - User Registration API

## Overview

Day 22 focused on building a User Registration API using FastAPI, SQLite, and Password Hashing.

Users can register accounts, and passwords are securely hashed before being stored in the database.

---

## Features

### Register User

```http
POST /register
```

Creates a new user account.

---

### View Users

```http
GET /users
```

Returns all registered users.

Passwords are not exposed.

---

## Database Schema

### Users Table

| Field | Type |
|---------|---------|
| id | Integer |
| username | Text |
| email | Text |
| password | Text (Hashed) |

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
- Password Hashing
- SQLite Database
- API Development
- Secure Password Storage

---

## Installation

Install password hashing library:

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
uvicorn user_registration_api:app --reload
```

---

## Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```json
{
    "username": "saurabh",
    "email": "saurabh@gmail.com",
    "password": "admin123"
}
```

---

## Learning Outcome

Day 22 helped me understand how user registration systems work in real-world applications. I learned how to securely store user credentials using password hashing and how to manage user data through APIs and databases.

---

## Next Step

Day 23:

- User Login API
- Password Verification
- Authentication Flow
- JWT Basics